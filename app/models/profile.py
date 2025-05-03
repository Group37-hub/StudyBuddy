from app import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subjects = db.Column(db.String, nullable=False)
    days_of_week = db.Column(db.String, nullable=False)
    availability = db.Column(db.String, nullable=False)
    preferred_gender = db.Column(db.String, nullable=True)
    location_details = db.Column(db.String, nullable=False)