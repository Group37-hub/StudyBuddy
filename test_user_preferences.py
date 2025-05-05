from models.user import User
from models.study_preferences import StudyPreferences


def test_update_study_preferences_success():
    study_preferences = StudyPreferences("1st", "Computer Science", "Male", "Morning", "Library")
    user = User("Andrew", study_preferences)

    user.update_study_preferences(
        year="2nd",
        subject="Physics",
        gender="Female",
        time="Evening",
        location="Cafe"
    )

    assert user.study_preferences.year == "2nd"
    assert user.study_preferences.subject == "Physics"
    assert user.study_preferences.gender == "Female"
    assert user.study_preferences.time == "Evening"
    assert user.study_preferences.location == "Cafe"


def test_update_study_preferences_no_changes():
    preferences = StudyPreferences("2nd", "Physics", "Female", "Afternoon", "Online")
    user = User("Alice", preferences)

    user.update_study_preferences()
    assert user.study_preferences.year == "2nd"
    assert user.study_preferences.subject == "Physics"
    assert user.study_preferences.gender == "Female"
    assert user.study_preferences.time == "Afternoon"
    assert user.study_preferences.location == "Online"
