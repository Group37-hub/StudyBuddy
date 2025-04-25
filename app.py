from flask import Flask, render_template, request, redirect, url_for
from models.user import User
from models.study_preferences import StudyPreferences

app = Flask(__name__)
app.debug = True

user = User(
    "Andrew",
    StudyPreferences("1st", "Computer Science", "Male", "Morning", "Library")
)


@app.route('/')
def home():
    return render_template('home.html')


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


if __name__ == '__main__':
    app.run(debug=True)
