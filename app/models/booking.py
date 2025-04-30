from datetime import datetime, timedelta
from app import db

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
