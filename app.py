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

@app.route('/edit_preferences', methods=['GET', 'POST'])
def edit_preferences():
    if request.method == 'POST':

        user.update_study_preferences(
            year      = request.form['year'],
            subject   = request.form['subject'],
            gender    = request.form['gender'],
            time      = request.form['time'],
            location  = request.form['location']
        )
        return redirect(url_for('home'))


    return render_template('profile.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)

