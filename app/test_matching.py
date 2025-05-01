# test_matching.py

import pandas as pd
from app.algorithm.similarity import preprocess_users, compute_similarity
from app.algorithm.main import find_top_matches

def test_matching_positive():
    """
    Positive Test Case: Verify that the matching algorithm returns the correct top matches
    for a user based on similarity scores.
    """
    # Mock data
    users_df = pd.DataFrame([
        {"user_id": 1, "name": "John", "subjects": ["Math"], "days_of_week": ["Monday"], "availability": ["Morning"], "preferred_gender": "Female", "location_details": ["Library"]},
        {"user_id": 2, "name": "Alice", "subjects": ["Math"], "days_of_week": ["Monday"], "availability": ["Morning"], "preferred_gender": "Female", "location_details": ["Library"]},
        {"user_id": 3, "name": "Bob", "subjects": ["Physics"], "days_of_week": ["Tuesday"], "availability": ["Afternoon"], "preferred_gender": "Male", "location_details": ["Cafe"]}
    ])
    processed_users = preprocess_users(users_df)
    weights = {"subjects": 0.5, "days_of_week": 0.2, "availability": 0.2, "preferred_gender": 0.1, "location_details": 0.1}
    similarity_matrix = compute_similarity(processed_users, weights)

    # Test top match for user_id=1
    matches = find_top_matches(1, similarity_matrix, users_df, top_k=1)
    assert len(matches) == 1
    assert matches[0]["match_user_id"] == 2  # Alice is the best match

def test_matching_negative():
    """
    Negative Test Case: Verify that the matching algorithm handles a user ID
    that does not exist in the dataset.
    """
    # Mock data
    users_df = pd.DataFrame([
        {"user_id": 1, "name": "John", "subjects": ["Math"], "days_of_week": ["Monday"], "availability": ["Morning"], "preferred_gender": "Female", "location_details": ["Library"]},
        {"user_id": 2, "name": "Alice", "subjects": ["Math"], "days_of_week": ["Monday"], "availability": ["Morning"], "preferred_gender": "Female", "location_details": ["Library"]}
    ])
    processed_users = preprocess_users(users_df)
    weights = {"subjects": 0.5, "days_of_week": 0.2, "availability": 0.2, "preferred_gender": 0.1, "location_details": 0.1}
    similarity_matrix = compute_similarity(processed_users, weights)

    # Test invalid user_id
    try:
        find_top_matches(99, similarity_matrix, users_df, top_k=1)
    except ValueError as e:
        assert str(e) == "User ID 99 not found in users_df"