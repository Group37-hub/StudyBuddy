import pytest
from app import app, db
from app.models import User

#set up test client (browser) and users in an in-memory database
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.drop_all() #to drop any previous users
            db.create_all()
            user1 = User(name="User1", email="user1@example.com")
            user2 = User(name="User2", email="user2@example.com")
            db.session.add_all([user1, user2])
            db.session.commit()
        yield client

#Positive test case: user1 sends a valid message to user2
def test_send_valid_message(client):
    #log in user1 by setting their user_id in the session
    with client.session_transaction() as sess:
        sess['user_id'] = 1  #assuming user1's ID is 1

    #check message appears on page
    response = client.post('/messages/2', data={'message': 'Hi there, want to study together?'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Hi there, want to study together?' in response.data

#Negative test case: user1 tries to send an empty message
def test_send_empty_message(client):
    #log in user1 by setting their user_id in the session
    with client.session_transaction() as sess:
        sess['user_id'] = 1

    #check if form validation fails (from forms.py) and error appears
    response = client.post('/messages/2', data={'message': ''}, follow_redirects=True)
    assert response.status_code == 200
    assert b'This field is required' in response.data