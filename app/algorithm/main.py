from app import User, Profile
from .data import load_mock_users
from .similarity import preprocess_users, compute_similarity
from .weights import QLearningWeightAdjuster
import pandas as pd


def initialize_algorithm(exclude_user_id=None):
    """Initialize the algorithm with default weights and load data."""
    users = User.query.all()
    profiles = Profile.query.all()

    users_data = [
        {
            "user_id": user.id,
            "name": user.name,
            "subjects": profile.subjects.split(","),
            "days_of_week": profile.days_of_week.split(","),
            "availability": profile.availability.split(","),
            "preferred_gender": profile.preferred_gender,
            "location_details": profile.location_details.split(","),
        }
        for user, profile in zip(users, profiles)
        if profile and (exclude_user_id is None or user.id != exclude_user_id)
    ]

    users_df = pd.DataFrame(users_data)

    # Preprocess user preferences into feature vectors
    processed_users = preprocess_users(users_df)

    # Initialize Q-learning agent with default weights
    q_agent = QLearningWeightAdjuster(
        initial_weights={
            "subjects": 0.5,
            "availability": 0.3,
            "days_of_week": 0.4,
            "preferred_gender": 0.2,
            "location_details": 0.6
        }
    )

    return users_df, processed_users, q_agent

def find_top_matches(target_user_id, similarity_matrix, users_df, top_k=3):
    """Find top-k matches for a given user."""
    # Mapping of user IDs to matrix indices
    index_to_user_id = users_df["user_id"].tolist()
    user_id_to_index = {uid: i for i, uid in enumerate(index_to_user_id)}

    # Skip if user_id isn't in similarity matrix
    if target_user_id not in user_id_to_index:
        raise ValueError(f"User ID {target_user_id} not found in users_df")

    user_index = user_id_to_index[target_user_id]
    similarities = similarity_matrix[user_index]

    matches = []
    for i, score in enumerate(similarities):
        match_user_id = index_to_user_id[i]
        if match_user_id == target_user_id:
            continue  # Skip self-match

        match_row = users_df.loc[users_df["user_id"] == match_user_id].iloc[0]
        target_row = users_df.loc[users_df["user_id"] == target_user_id].iloc[0]

        shared_subjects = list(set(target_row["subjects"]) & set(match_row["subjects"]))

        matches.append({
            "match_user_id": match_user_id,
            "name": match_row["name"],
            "score": score,
            "shared_subjects": shared_subjects
        })

    # Sort and return top-k
    matches = sorted(matches, key=lambda x: x["score"], reverse=True)[:top_k]
    return matches



def main():
    """Main function to run the study buddy matching algorithm."""
    # Step 1: Initialize data and algorithm
    users_df, processed_users, q_agent = initialize_algorithm()


if __name__ == "__main__":
    main()