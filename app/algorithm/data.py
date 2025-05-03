import pandas as pd

def load_mock_users():
    """Mock data with updated schema."""
    mock_users = [
        {
            "id": 1,
            "user_id": 1,
            "name": "John",
            "subjects": ["Physics", "Mathematics"],
            "days_of_week": ["Monday", "Tuesday"],
            "availability": ["Morning (8-11 AM)"],
            "preferred_gender": "Female",
            "location_details": ["Library"]
        },
        {
            "id": 2,
            "user_id": 2,
            "name": "Alice",
            "subjects": ["Biology", "Chemistry"],
            "days_of_week": ["Wednesday", "Thursday"],
            "availability": ["Afternoon (12-3 PM)"],
            "preferred_gender": "Male",
            "location_details": ["Cafe"]
        },
        {
            "id": 3,
            "user_id": 3,
            "name": "Bob",
            "subjects": ["Mathematics", "Physics"],
            "days_of_week": ["Monday", "Friday"],
            "availability": ["Evening (4-7 PM)"],
            "preferred_gender": "No Preference",
            "location_details": ["Zoom"]
        },
        {
            "id": 4,
            "user_id": 4,
            "name": "Charlie",
            "subjects": ["Data Science", "Machine Learning"],
            "days_of_week": ["Tuesday", "Thursday"],
            "availability": ["Morning (8-11 AM)"],
            "preferred_gender": "Female",
            "location_details": ["Library"]
        },
        {
            "id": 5,
            "user_id": 5,
            "name": "Diana",
            "subjects": ["English", "History"],
            "days_of_week": ["Wednesday", "Friday"],
            "availability": ["Afternoon (12-3 PM)"],
            "preferred_gender": "Male",
            "location_details": ["Teams"]
        },
        {
            "id": 6,
            "user_id": 6,
            "name": "Eve",
            "subjects": ["Physics", "Mathematics"],
            "days_of_week": ["Monday", "Saturday"],
            "availability": ["Morning (8-11 AM)"],
            "preferred_gender": "No Preference",
            "location_details": ["Library"]
        },
        {
            "id": 7,
            "user_id": 7,
            "name": "Frank",
            "subjects": ["Biology", "Chemistry"],
            "days_of_week": ["Tuesday", "Thursday"],
            "availability": ["Evening (4-7 PM)"],
            "preferred_gender": "Female",
            "location_details": ["Cafe"]
        },
        {
            "id": 8,
            "user_id": 8,
            "name": "Grace",
            "subjects": ["Data Science", "Machine Learning"],
            "days_of_week": ["Monday", "Wednesday"],
            "availability": ["Afternoon (12-3 PM)"],
            "preferred_gender": "Male",
            "location_details": ["Zoom"]
        },
        {
            "id": 9,
            "user_id": 9,
            "name": "Hank",
            "subjects": ["English", "History"],
            "days_of_week": ["Friday", "Saturday"],
            "availability": ["Morning (8-11 AM)"],
            "preferred_gender": "No Preference",
            "location_details": ["Teams"]
        },
        {
            "id": 10,
            "user_id": 10,
            "name": "Ivy",
            "subjects": ["Physics", "Mathematics"],
            "days_of_week": ["Monday", "Tuesday"],
            "availability": ["Evening (4-7 PM)"],
            "preferred_gender": "Female",
            "location_details": ["Library"]
        }
    ]
    return pd.DataFrame(mock_users)