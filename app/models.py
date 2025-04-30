from datetime import datetime, timedelta
from werkzeug.security import check_password_hash, generate_password_hash

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #password = db.Column(db.String(128), nullable=False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    #flag for if the message should be kept or discarded (default is True)
    keep = db.Column(db.Boolean, default=True)

    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    #link sender to messages they've sent
    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_messages')
    ##link receiver to messages they've received
    receiver = db.relationship('User', foreign_keys=[receiver_id], backref='received_messages')

    def __repr__(self):
        return '<Message {}>'.format(self.content)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(100), unique=True, nullable=False)
    building = db.Column(db.String(200), nullable=True)
    capacity = db.Column(db.Integer, nullable=False)
    bookings = db.relationship('Booking', backref='room', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    week_beginning = db.Column(db.DateTime, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    hour = db.Column(db.Integer, nullable=False)
    booking_end = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.String(20), nullable=False, default='pending')

    def get_booking_end(self):
        booking_end = datetime.combine(self.week_beginning, datetime.min.time()) + timedelta(days=self.day,hours=self.hour+1)
        return booking_end

    def is_past(self):
        return self.booking_end < datetime.now()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.week_beginning:
            today = datetime.now()
            monday = today - timedelta(days=today.weekday())
            self.week_beginning = monday.date()

        self.booking_end = self.get_booking_end()
