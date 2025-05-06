from datetime import datetime

import pytest
from app import app, db
from app.models import User, Room, Booking
from app.views import get_week_beginning


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config["WTF_CSRF_ENABLED"] = False

    with app.app_context():
        db.drop_all()
        db.create_all()
        user1 = User(name="User1", email="user1@example.com")
        user2 = User(name="User2", email="user2@example.com")
        db.session.add_all([user1, user2])
        room = Room(room_name="Study Room 1", building = "Computer Science", capacity=10)
        db.session.add(room)
        db.session.commit()

        with app.test_client() as client:
            yield client

# positive case for room booking
def test_successful_room_booking(client):
    with client.session_transaction() as sess:
        sess['user_id'] = 1
    week_beginning = get_week_beginning()
    tomorrow = get_tomorrow()
    response = client.post("/book-room", data={
        "room_id": 1,
        "day": tomorrow,
        "hour": 10,
        "week_beginning": week_beginning,
        "user1_id": 1,
        "user2_id": 2,
        "submit": True
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Room added successfully" in response.data

    booking = Booking.query.filter_by(room_id=1, day=tomorrow, hour=10).first()
    assert booking is not None

# negative case for room booking
def test_booking_with_missing_data(client):
    with client.session_transaction() as sess:
        sess['user_id'] = 1
    week_beginning = get_week_beginning()
    tomorrow = get_tomorrow()
    response = client.post("/book-room", data={
        "room_id": 1,
        "day": tomorrow,
        "hour": None,
        "week_beginning": week_beginning,
        "user1_id": 1,
        "user2_id": 2,
        "submit": True
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Please fill in the form correctly" in response.data

# positive case for decline invitation
def test_decline_invitation(client):
    week_beginning = get_week_beginning()
    tomorrow = get_tomorrow()
    with app.app_context():
        booking = Booking(
            room_id=1,
            user1_id=1,
            user2_id=2,
            week_beginning=week_beginning,
            day=tomorrow,
            hour=10,
            status="pending"
        )
        db.session.add(booking)
        db.session.commit()
        booking_id = booking.id

    with client.session_transaction() as sess:
        sess['user_id'] = 2

    response = client.get(f"/decline_invitation/{booking_id}", follow_redirects=True)
    assert b"Invitation declined." in response.data

    with app.app_context():
        updated_booking = Booking.query.get(booking_id)
        assert updated_booking.status == "declined"

# negative case for decline invitation, user not logged in
def test_decline_invitation_negative(client):
    week_beginning = get_week_beginning()
    tomorrow = get_tomorrow()
    with app.app_context():
        booking = Booking(
            room_id=1,
            user1_id=1,
            user2_id=2,
            week_beginning=week_beginning,
            day=tomorrow,
            hour=10,
            status="pending"
        )
        db.session.add(booking)
        db.session.commit()
        booking_id = booking.id


    response = client.get(f"/decline_invitation/{booking_id}", follow_redirects=True)
    assert b"Please log in first." in response.data

# helper function
def get_tomorrow():
    # 8 days a week, incase you are testing on a Sunday
    tomorrow = (datetime.now().weekday() + 1) % 8
    return tomorrow

