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
    formatted_meeting_date = db.Column(db.String(20))

    # Finds when the booking is over
    def get_booking_end(self):
        booking_end = datetime.combine(self.week_beginning, datetime.min.time()) + timedelta(days=self.day,hours=self.hour+1)
        return booking_end

    # Checks if the booking is past
    def is_past(self):
        return self.booking_end < datetime.now()

    # Formats the meeting date
    def format_meeting_date(self):
        meeting_date = self.week_beginning + timedelta(days=self.day)
        day_name = meeting_date.strftime('%A')
        month_name = meeting_date.strftime('%B')
        day_with_suffix = self.get_ordinal()
        return f"{day_name} the {day_with_suffix} of {month_name}"

    def get_ordinal(self):
        if 11 <= self.day % 100 <= 13:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(self.day % 10, 'th')
        return f"{self.day}{suffix}"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.week_beginning:
            today = datetime.now()
            monday = today - timedelta(days=today.weekday())
            self.week_beginning = monday.date()

        self.booking_end = self.get_booking_end()
        self.formatted_meeting_date = self.format_meeting_date()
