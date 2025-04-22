from models.user import User
from models.study_preferences import StudyPreferences


def test_update_preferences():
    user = User("Test", StudyPreferences("1st", "Maths", "Girl", "Morning", "Library"))
    user.update_study_preferences(subject="Physics", time="Afternoon", location="Cafe")
    assert user.study_preferences.subject == "Physics"
    assert user.study_preferences.time == "Afternoon"
    assert user.study_preferences.location == "Cafe"


def test_invalid_gender():
    user = User("Test", StudyPreferences("1st", "Maths", "Girl"))
    user.update_study_preferences(gender="unknown")
    assert user.study_preferences.gender == "Girl"  # should not change
