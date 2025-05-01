# class User:
#     def __init__(self, name, email, study_preferences):
#         self.name = name
#         self.email = email
#         self.study_preferences = study_preferences
#
#     def update_study_preferences(self, year=None, subject=None, gender=None, time=None, location=None):
#         if year:
#             self.study_preferences.year = year
#         if subject:
#             self.study_preferences.subject = subject
#         if gender in ("Female", "Male", "Either"):
#             self.study_preferences.gender = gender
#         if time:
#             self.study_preferences.time = time
#         if location:
#             self.study_preferences.location = location
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
