from models.study_preferences import StudyPreferences


class User:
    def __init__(self, name, study_preferences):
        self.name = name
        self.study_preferences = study_preferences

    def update_study_preferences(self, year=None, subject=None, gender=None, time=None, location=None):
        if year:
            self.study_preferences.year = year
        if subject:
            self.study_preferences.subject = subject
        if gender in ("Female", "Male", "Either"):
            self.study_preferences.gender = gender
        if time:
            self.study_preferences.time = time
        if location:
            self.study_preferences.location = location
