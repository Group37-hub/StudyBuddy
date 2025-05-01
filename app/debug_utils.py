from app import db
import datetime

from app.models.booking import Booking
from app.models.message import Message
from app.models.room import Room
from app.models.user import User


def reset_db():
    db.drop_all()
    db.create_all()

def test_data():
    u1 = User(name="Iona", email="iona@iona.com")
    db.session.add(u1)
    db.session.commit()

    u2 = User(name="Izzy", email="izzy@izzy.com")
    db.session.add(u2)
    db.session.commit()

    u3 = User(name="Isla", email="isla@isla.com")
    db.session.add(u3)
    db.session.commit()

    u4 = User(name="Irene", email="irene@irene.com")
    db.session.add(u4)
    db.session.commit()

    m1 = Message(content="I love eggs", sender_id=u1.id, receiver_id=u2.id)
    db.session.add(m1)
    db.session.commit()

    r1 = Room(room_name = "CS1", building = "Computer Science", capacity = 100)
    db.session.add(r1)
    db.session.commit()

    r2 = Room(room_name="CS2", building="Computer Science", capacity=100)
    db.session.add(r2)

    b1 = Booking(user1_id = u1.id, user2_id = u2.id, room_id = r1.id, week_beginning = datetime.datetime.now(), day = 1, hour = 11, status = "pending")
    db.session.add(b1)
    db.session.commit()
