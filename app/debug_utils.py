from app.models import User, Profile
from app.algorithm.data import load_mock_users

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
                email=f"{user_data['name'].lower()}@example.com"
            )
            db.session.add(user)

            profile = Profile(
                user_id=user_data["user_id"],
                subjects=",".join(user_data["subjects"]),
                days_of_week=",".join(user_data["days_of_week"]),
                availability=",".join(user_data["availability"]),
                preferred_gender=user_data["preferred_gender"],  # Updated field
                location_details=",".join(user_data["location_details"])
            )
            db.session.add(profile)

        db.session.commit()
        print("Database has been reset and mock data has been added.")
    except Exception as e:
        print(f"Error during reset_db: {e}")
        db.session.rollback()