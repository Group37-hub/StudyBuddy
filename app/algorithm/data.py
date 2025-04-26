# app/algorithm/data.py
import pandas as pd

def load_mock_users():
    """Mock data with names and preferences."""
    mock_users = [
        {
            "id": 1,
            "user_id": 1,
            "name": "John",
            "subjects": ["Physics", "Mathematics"],
            "days_of_week": ["Monday", "Tuesday"],
            "availability": ["Morning (8-11 AM)"],
            "learning_style": "Visual",
            "location_type": {"Virtual"},
            "location_details": {"Zoom"}
        },
        {
            "id": 2,
            "user_id": 11,
            "name": "Alice",
            "subjects": ["Math", "Machine Learning"],
            "days_of_week": ["Monday", "Wednesday"],
            "availability": ["Mornings", "Afternoons"],
            "learning_style": "Visual",
            "location_type": {"In-person"},
            "location_details": {"Library"}
        },
        {
            "id": 3,
            "user_id": 2,
            "name": "Bob",
            "subjects": ["Machine Learning", "Physics"],
            "days_of_week": ["Monday", "Wednesday"],
            "availability": ["Evenings"],
            "learning_style": "Hands-on",
            "location_type": {"Virtual"},
            "location_details": {"Slack"}
        },
        {
            "id": 4,
            "user_id": 3,
            "name": "Charlie",
            "subjects": ["Math", "Data Science"],
            "days_of_week": ["Monday", "Wednesday"],
            "availability": ["Mornings"],
            "learning_style": "Auditory",
            "location_type": {"In-person"},
            "location_details": {"Library"}
        },
        {
            "id": 5,
            "user_id": 4,
            "name": "Diana",
            "subjects": ["Biology", "Chemistry"],
            "days_of_week": ["Tuesday", "Thursday"],
            "availability": ["Afternoons"],
            "learning_style": "Reading/Writing",
            "location_type": {"Virtual"},
            "location_details": {"Teams"}
        },
        {
            "id": 6,
            "user_id": 5,
            "name": "Eve",
            "subjects": ["Physics", "Mathematics"],
            "days_of_week": ["Friday", "Saturday"],
            "availability": ["Mornings"],
            "learning_style": "Visual",
            "location_type": {"In-person"},
            "location_details": {"Library"}
        },
        {
            "id": 7,
            "user_id": 6,
            "name": "Frank",
            "subjects": ["Data Science", "Machine Learning"],
            "days_of_week": ["Monday", "Tuesday"],
            "availability": ["Evenings"],
            "learning_style": "Hands-on",
            "location_type": {"Virtual"},
            "location_details": {"Zoom"}
        },
        {
            "id": 8,
            "user_id": 7,
            "name": "Grace",
            "subjects": ["English", "History"],
            "days_of_week": ["Wednesday", "Thursday"],
            "availability": ["Afternoons"],
            "learning_style": "Auditory",
            "location_type": {"In-person"},
            "location_details": {"Library"}
        },
        {
            "id": 9,
            "user_id": 8,
            "name": "Hank",
            "subjects": ["Mathematics", "Physics"],
            "days_of_week": ["Monday", "Friday"],
            "availability": ["Mornings"],
            "learning_style": "Visual",
            "location_type": {"Virtual"},
            "location_details": {"Slack"}
        },
        {
            "id": 10,
            "user_id": 9,
            "name": "Ivy",
            "subjects": ["Biology", "Chemistry"],
            "days_of_week": ["Tuesday", "Thursday"],
            "availability": ["Evenings"],
            "learning_style": "Reading/Writing",
            "location_type": {"In-person"},
            "location_details": {"Teams"}
        },
        {
            "id": 11,
            "user_id": 10,
            "name": "Jack",
            "subjects": ["Physics", "Data Science"],
            "days_of_week": ["Monday", "Wednesday"],
            "availability": ["Afternoons"],
            "learning_style": "Hands-on",
            "location_type": {"Virtual"},
            "location_details": {"Zoom"}
        }
    ]
    return pd.DataFrame(mock_users)