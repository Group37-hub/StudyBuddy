from flask import render_template, request, flash, redirect, url_for, session
from app import app, db
from app.forms import MessageForm, LoginForm
from app.models import Message, User

@app.route("/")
def home():
    return render_template('home.html', title="Home")

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

    if form.validate_on_submit():
        content = form.message.data
        msg = Message(sender_id=current_user_id, receiver_id=user_id, content=content)
        db.session.add(msg)
        db.session.commit()
        flash("Message sent!")
        return redirect(url_for("messages", user_id=user_id))

    all_messages = Message.query.filter(
        ((Message.sender_id == current_user_id) & (Message.receiver_id == user_id)) |
        ((Message.sender_id == user_id) & (Message.receiver_id == current_user_id)),
        Message.keep == True
    ).order_by(Message.timestamp.asc()).all()

    return render_template("message.html", messages=all_messages, other_user=other_user, form=form, title="Messages",current_user_id=current_user_id)

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
