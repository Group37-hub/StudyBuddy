# algorithm/data.py
import pandas as pd

def load_mock_users():
    """Mock data with location (in-person or virtual + details)"""
    mock_users = [
        {
            "id": 2,
            "user_id": 10,
            "subjects": ["Math", "Machine Learning"],
            "days_of_week": ["Monday", "Wednesday"],
            "availability": ["mornings", "afternoons"],
            "learning_style": "visual",
            "location_type": {"in-person"},
            "location_details": {"Library"}
        },
        {
            "id": 3,
            "user_id": 2,
            "subjects": ["Machine Learning", "Physics"],
            "days_of_week": ["Monday", "Wednesday"],
            "availability": ["evenings"],
            "learning_style": "hands-on",
            "location_type": {"virtual"},
            "location_details": {"Slack"}
        },
        {
            "id": 4,
            "user_id": 3,
            "subjects": ["Math", "Data Science"],
            "days_of_week": ["Monday", "Wednesday"],
            "availability": ["mornings"],
            "learning_style": "auditory",
            "location_type": {"in-person"},
            "location_details": {"Library"}
        }
    ]
    return pd.DataFrame(mock_users)