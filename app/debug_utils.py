from werkzeug.security import generate_password_hash

from app.models import User, Profile
from app.algorithm.data import load_mock_users, load_mock_rooms
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
    mock_rooms = load_mock_rooms()
    print("Mock rooms loaded:", mock_rooms)

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
            
        for room_data in mock_rooms:
            room = Room(**room_data)
            db.session.add(room)
        db.session.commit()
        print("Database has been reset and mock data has been added.")
        
    except Exception as e:
        print(f"Error during reset_db: {e}")
        db.session.rollback()


