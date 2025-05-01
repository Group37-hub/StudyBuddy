from datetime import datetime, timedelta

import flask

from app import app, db
from flask import Flask, render_template, request, session, flash, redirect, url_for

from app.forms import LoginForm, MessageForm, BookingForm
from app.models import user
from app.models.booking import Booking
from app.models.message import Message
from app.models.room import Room
from app.models.user import User
from app.models.study_preferences import StudyPreferences

# user = User(
#     "Andrew",
#     StudyPreferences("1st", "Computer Science", "Male", "Morning", "Library")
# )


@app.route("/")
def home():
    return render_template('home.html', title="Home")


@app.route('/edit_preferences', methods=['GET', 'POST'])
def edit_preferences():
    success = None
    if request.method == 'POST':
        year = request.form.get('year')
        subject = request.form.get('subject')
        gender = request.form.get('gender')
        time_pref = request.form.get('time')
        location = request.form.get('location')

        # user.update_study_preferences(
        #         year=year,
        #         subject=subject,
        #         gender=gender,
        #         time=time_pref,
        #         location=location
        #     )
        success = "Study preferences updated successfully!"
        return render_template('profile.html', user=user, success=success)
    return render_template('profile.html', user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            session["user_id"] = user.id
            flash(f"Logged in as {user.name}", "success")
            return redirect(url_for("home"))
        else:
            flash("User not found", "danger")
    return render_template("login.html", form=form, title="Login")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out", "info")
    return redirect(url_for("home"))

@app.route("/messages/<int:user_id>", methods=["GET", "POST"])
def messages(user_id):
    if "user_id" not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    current_user_id = session["user_id"]
    other_user = User.query.get_or_404(user_id)
    form = MessageForm()
    booking_form = BookingForm()

    if form.validate_on_submit():
        content = form.message.data
        msg = Message(sender_id=current_user_id, receiver_id=user_id, content=content)
        db.session.add(msg)
        db.session.commit()
        flash("Message sent!", "success")
        return redirect(url_for("messages", user_id=user_id))

    all_messages = Message.query.filter(
        ((Message.sender_id == current_user_id) & (Message.receiver_id == user_id)) |
        ((Message.sender_id == user_id) & (Message.receiver_id == current_user_id)),
        Message.keep == True
    ).order_by(Message.timestamp.asc()).all()

    # ─────────────── Booking Logic ─────────────── #

    upcoming_booking = None
    pending_invitation = None
    user2_booking_invite = None
    declined_invitation = None
    most_recent_booking_date = None
    most_recent_booking = None

    # Get all current bookings

    all_bookings = Booking.query.filter(
        ((Booking.user1_id== current_user_id) & (Booking.user2_id == other_user.id)) |
        ((Booking.user1_id == other_user.id) & (Booking.user2_id == current_user_id)),
        Booking.status != 'past'
    ).all()

    # Find relevant booking to display
    for booking in all_bookings:
        # Find the most recent booking by when it was created
        if not most_recent_booking_date or booking.created_at > most_recent_booking_date:
            most_recent_booking_date = booking.created_at
            most_recent_booking = booking

        if booking.is_past():
            booking.status = "past"
            db.session.commit()
        elif booking.user1_id == current_user_id and booking.status == "pending":
            pending_invitation = booking
        elif booking.status == "accepted":
            upcoming_booking = booking
        elif booking.user2_id == current_user_id and booking.status == "pending":
            user2_booking_invite = booking

    # Find if the most recent booking was declined
    if most_recent_booking and most_recent_booking.status == "declined":
            declined_invitation = most_recent_booking

    # Set up booking form choices
    rooms = Room.query.all()
    booking_form.room_id.choices = [(room.id, room.room_name) for room in rooms]
    booking_form.user1_id.data = current_user_id
    booking_form.user2_id.data = other_user.id
    booking_form.week_beginning.data = get_week_beginning().date()
    booking_form.hour.choices = [(hour, f"{hour}:00") for hour in range(9, 17)]


    return render_template("message.html", messages=all_messages, other_user=other_user,
                           form=form, booking_form = booking_form, title="Messages",current_user_id=current_user_id,
                           study_invitation = user2_booking_invite, pending_invitation = pending_invitation,
                           upcoming_booking = upcoming_booking, declined_invitation = declined_invitation)

@app.route("/book-room", methods=["POST"])
def book_room():
    form = BookingForm()
    rooms = Room.query.all()
    form.room_id.choices = [(room.id, room.room_name) for room in rooms]
    room_id = form.room_id.data
    week_beginning = form.week_beginning.data
    day = form.day.data

    # Update available hours
    if room_id and week_beginning is not None and day is not None:
        form.hour.choices = get_available_hours(room_id, week_beginning, day)

    # Create booking
    if form.validate_on_submit():
        user2_id = form.user2_id.data
        user1_id = form.user1_id.data
        week_beginning = form.week_beginning.data
        room_id = form.room_id.data
        day = form.day.data
        hour = form.hour.data

        # Check if the room is available
        existing_booking = Booking.query.filter_by(
            room_id=room_id,
            week_beginning=week_beginning,
            day=day,
            hour=hour
        ).filter(
            Booking.status.in_(['accepted', 'pending'])
        ).first()

        if existing_booking:
            flash("Room not available at this time", "warning")
            return redirect(url_for("messages", user_id=user2_id))

        new_booking = Booking(
            room_id=room_id,
            user1_id=user1_id,
            user2_id=user2_id,
            week_beginning=week_beginning,
            day=day,
            hour=hour
        )
        db.session.add(new_booking)
        db.session.commit()
        flash("Room added successfully", "success")

        return redirect(url_for('messages', user_id=user2_id))
    return redirect(url_for('messages', user_id=form.user2_id))

@app.route("/delete_message/<int:msg_id>")
def delete_message(msg_id):
    if "user_id" not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    current_user_id = session["user_id"]
    msg = Message.query.get_or_404(msg_id)
    if msg.sender_id == current_user_id or msg.receiver_id == current_user_id:
        msg.keep = False
        db.session.commit()
        flash("Message deleted.")
    return redirect(url_for("messages", user_id=msg.receiver_id if msg.sender_id == current_user_id else msg.sender_id))

# ─────────────── Booking invitation response functions ─────────────── #
@app.route("/decline_invitation/<int:booking_id>")
def decline_invitation(booking_id):
    booking = Booking.query.get_or_404(booking_id)

    if "user_id" not in session:
        return redirect(url_for("messages", user_id=booking.user1_id))

    booking.status = "declined"
    db.session.commit()
    flash("Invitation declined.", "info")

    return redirect(url_for("messages", user_id=booking.user1_id))
@app.route("/delete_invitation/<int:booking_id>")
def cancel_invitation(booking_id):
    booking = Booking.query.get_or_404(booking_id)

    if "user_id" not in session:
        return redirect(url_for("messages", user_id=booking.user2_id))

    booking.status = "cancelled"
    db.session.commit()
    flash("Invitation canceled.", "info")

    return redirect(url_for("messages", user_id=booking.user2_id))

@app.route("/accept_invitation/<int:booking_id>")
def accept_invitation(booking_id):
    if "user_id" not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    current_user_id = session["user_id"]
    booking = Booking.query.get_or_404(booking_id)

    if current_user_id != booking.user2_id:
        return redirect(url_for("home"))

    booking.status = "accepted"
    db.session.commit()
    flash("Invitation accepted.", "success")

    return redirect(url_for("messages", user_id=booking.user1_id))

# ─────────────── Helper functions ─────────────── #

def get_week_beginning():
    # Returns the start of the week
    today = datetime.today()
    return today - timedelta(days=today.weekday())

def get_available_hours(room_id, week_beginning, day):
    # Gets available hours for rooms
    all_hours = list(range(9, 17))

    booked = Booking.query.filter(
        Booking.room_id == room_id,
        Booking.week_beginning == week_beginning,
        Booking.day == day,
        Booking.status.in_(['accepted', 'pending'])
    ).with_entities(Booking.hour).all()

    booked_hours = {booking.hour for booking in booked}
    return [(hour, f"{hour}:00") for hour in all_hours if hour not in booked_hours]

# Error handlers
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# Error handler for 403 Forbidden
@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html', title='Error'), 403

# Handler for 404 Not Found
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', title='Error'), 404

@app.errorhandler(413)
def error_413(error):
    return render_template('errors/413.html', title='Error'), 413

# 500 Internal Server Error
@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html', title='Error'), 500
