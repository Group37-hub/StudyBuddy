from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    profile = db.relationship('Profile', backref='user', uselist=False)

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subjects = db.Column(db.String, nullable=False)
    days_of_week = db.Column(db.String, nullable=False)
    availability = db.Column(db.String, nullable=False)
    learning_style = db.Column(db.String, nullable=False)
    location_type = db.Column(db.String, nullable=False)
    location_details = db.Column(db.String, nullable=False)