from app import app
from flask import Flask, render_template, request

from app.models.user import User
from app.models.study_preferences import StudyPreferences

user = User(
    "Andrew",
    StudyPreferences("1st", "Computer Science", "Male", "Morning", "Library")
)


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

        user.update_study_preferences(
                year=year,
                subject=subject,
                gender=gender,
                time=time_pref,
                location=location
            )
        success = "Study preferences updated successfully!"
        return render_template('profile.html', user=user, success=success)
    return render_template('profile.html', user=user)




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