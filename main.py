from models.user import User
from models.study_preferences import StudyPreferences

all_users = [
    User("Tyra", StudyPreferences("1st", "Computer Science", "Girl", "Morning", "Library")),
    User("Ashley", StudyPreferences("2nd", "Physics", "Boy", "Afternoon", "Study Room")),
    User("Robert", StudyPreferences("1st", "Computer Science", "Boy", "Evening", "Cafe"))
]

user1 = User("Andrew", StudyPreferences("1st", "Computer Science", "Boy", "Evening", "Library"))

print("Initial preferences:")
print(user1.study_preferences.__dict__)

print("\nUpdating preferences...")
user1.update_study_preferences(subject="Maths", time="Morning", location="Cafe")
print(user1.study_preferences.__dict__)
