from flask import Flask, render_template, request, redirect, url_for
from models.user import User
from models.study_preferences import StudyPreferences

app = Flask(__name__)


user = User(
    "Andrew",
    StudyPreferences("1st", "Computer Science", "Male", "Morning", "Library")
)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/edit_preferences', methods=['GET', 'POST'])
def edit_preferences():
    if request.method == 'POST':
        year = request.form['year']
        subject = request.form['subject']
        gender = request.form['gender']
        time_preference = request.form['time']
        location = request.form['location']

        user.update_study_preferences(
            year=year,
            subject=subject,
            gender=gender,
            time=time_preference,
            location=location
        )

        success = "Your preferences have been updated successfully!"
        return render_template('profile.html', user=user, success=success)

    return render_template('profile.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
