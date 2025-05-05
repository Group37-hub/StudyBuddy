from werkzeug.security import generate_password_hash

from app.models import User, Profile
from app.algorithm.data import load_mock_users
from app import db
import datetime

from app.models.booking import Booking
from app.models.message import Message
from app.models.room import Room
from app.models.user import User


def reset_db():
    from app import db
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()
    print("Tables created successfully:")

    # Load mock data
    mock_users = load_mock_users()
    print("Mock users loaded:", mock_users)

    try:
        for _, user_data in mock_users.iterrows():
            user = User(
                id=user_data["user_id"],
                name=user_data["name"],
                email=f"{user_data['name'].lower()}@student.bham.ac.uk",
                password = generate_password_hash("default_password")
            )
            db.session.add(user)

            profile = Profile(
                user_id=user_data["user_id"],
                subjects=",".join(user_data["subjects"]),
                days_of_week=",".join(user_data["days_of_week"]),
                availability=",".join(user_data["availability"]),
                preferred_gender=user_data["preferred_gender"],
                location_details=",".join(user_data["location_details"])
            )
            db.session.add(profile)

        db.session.commit()
        print("Database has been reset and mock data has been added.")
    except Exception as e:
        print(f"Error during reset_db: {e}")
        db.session.rollback()

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

