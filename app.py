from flask import Flask, render_template, request, redirect, url_for
from models.user import User
from models.study_preferences import StudyPreferences

app = Flask(__name__)

# Simulated user data
users = [
    User("Andrew", StudyPreferences("1st", "Computer Science", "Male")),
    User("Tyra", StudyPreferences("1st", "Physics", "Female"))
]


@app.route('/')
def home():
    """Render the homepage"""
    return render_template("home.html")


@app.route('/edit_preferences', methods=["GET", "POST"])
def edit_preferences():
    """Render the profile editing form and handle form submissions"""
    user = users[0]  # For simplicity, let's work with the first user (Andrew)

    if request.method == "POST":
        # Get new preferences from form data and update user
        user.update_study_preferences(
            year=request.form['year'],
            subject=request.form['subject'],
            gender=request.form['gender'],
            time=request.form['time'],
            location=request.form['location']
        )
        return redirect(url_for('home'))  # After submitting, return to home

    return render_template("profile.html", user=user)  # Render profile editing page


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/update_preferences', methods=['POST'])
def update_preferences():
    # Extract data from the form
    year = request.form['year']
    subject = request.form['subject']
    gender = request.form['gender']
    time = request.form['time']
    location = request.form['location']

    # Here, you would update the user's preferences in your backend (e.g., a database or in-memory object)
    # You could update the user preferences like this:
    user = get_logged_in_user()  # Fetch the logged-in user
    user.update_study_preferences(year, subject, gender, time, location)

    # Redirect or render the page to show the updated preferences
    return redirect(url_for('profile'))
