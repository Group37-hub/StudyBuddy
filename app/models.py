from datetime import datetime
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