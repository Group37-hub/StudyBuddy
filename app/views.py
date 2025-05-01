from app import app, db
from flask import render_template, request, redirect, url_for
from app.algorithm.main import initialize_algorithm, find_top_matches, compute_similarity
from app.models import User, Profile

@app.route("/")
def home():
    return render_template('home.html', title="Home")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template('login.html', title="Login")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    return render_template('chat.html', title="Chat")

@app.route('/edit_preferences', methods=['GET', 'POST'])
def edit_preferences():
    success = None
    user_id = 1  # Replace with the logged-in user's ID
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return "User not found", 404

    if request.method == 'POST':
        profile = Profile.query.filter_by(user_id=user_id).first()
        if not profile:
            profile = Profile(user_id=user_id)

        profile.subjects = ','.join(request.form.getlist('subjects'))
        profile.days_of_week = ','.join(request.form.getlist('days_of_week'))
        profile.availability = ','.join(request.form.getlist('availability'))
        profile.preferred_gender = request.form.get('preferred_gender')  # Updated field
        profile.location_details = ','.join(request.form.getlist('location_details'))

        db.session.add(profile)
        db.session.commit()
        success = "Preferences updated successfully!"
    return render_template('preference_form.html', title="Edit Preferences", success=success, user=user)

@app.route('/profile', methods=['GET'])
def profile():
    user_id = 1  # Replace with the logged-in user's ID
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return "User not found", 404

    users = User.query.all()
    profiles = Profile.query.all()

    users_data = [
        {
            "user_id": user.id,
            "name": user.name,
            "subjects": profile.subjects.split(","),
            "days_of_week": profile.days_of_week.split(","),
            "availability": profile.availability.split(","),
            "preferred_gender": profile.preferred_gender,  # Updated field
            "location_details": profile.location_details.split(","),
        }
        for user, profile in zip(users, profiles) if profile
    ]

    import pandas as pd
    users_df = pd.DataFrame(users_data)

    _, processed_users, q_agent = initialize_algorithm()
    similarity_matrix = compute_similarity(processed_users, q_agent.q_table)
    matches = find_top_matches(user_id, similarity_matrix, users_df, top_k=5)

    return render_template('profile.html', title="Your Profile", matches=matches, user=user)


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