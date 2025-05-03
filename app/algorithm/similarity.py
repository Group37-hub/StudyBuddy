# algorithm/similarity.py
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder
import pandas as pd


def preprocess_users(df):
    """Preprocess all features, including location"""
    # 1. Encode subjects (multi-label)
    mlb = MultiLabelBinarizer()
    # Encode subjects
    subjects_encoded = mlb.fit_transform(df['subjects'])
    subjects_df = pd.DataFrame(subjects_encoded, columns=[f"subject_{cls}" for cls in mlb.classes_])

    # Encode days_of_week
    days_of_week_encoded = mlb.fit_transform(df['days_of_week'])
    days_of_week_df = pd.DataFrame(days_of_week_encoded, columns=[f"days_of_week_{cls}" for cls in mlb.classes_])

    # Encode availability
    availability_encoded = mlb.fit_transform(df['availability'])
    availability_df = pd.DataFrame(availability_encoded, columns=[f"availability_{cls}" for cls in mlb.classes_])

    # Encode preferred_gender
    preferred_gender_df = pd.get_dummies(df['preferred_gender'], prefix='gender')

    # Encode location_details
    location_details_encoded = mlb.fit_transform(df['location_details'])
    location_details_df = pd.DataFrame(location_details_encoded, columns=[f"loc_details_{cls}" for cls in mlb.classes_])

    # Combine all features
    return pd.concat([subjects_df, days_of_week_df, availability_df, preferred_gender_df, location_details_df], axis=1)


def compute_similarity(users_df, weights):
    """Apply weights to all feature groups (including location)"""
    weighted_vectors = users_df.copy()

    # Identify columns for each feature group
    subject_cols = [col for col in users_df.columns if col.startswith("subject_")]
    days_of_week_cols = [col for col in users_df.columns if col.startswith("days_of_week_")]
    availability_cols = [col for col in users_df.columns if col.startswith("availability_")]
    gender_cols = [col for col in users_df.columns if col.startswith("gender_")]
    loc_details_cols = [col for col in users_df.columns if col.startswith("loc_details_")]

    # Apply weights
    weighted_vectors[subject_cols] *= weights["subjects"]
    weighted_vectors[days_of_week_cols] *= weights["days_of_week"]
    weighted_vectors[availability_cols] *= weights["availability"]
    weighted_vectors[gender_cols] *= weights["preferred_gender"]
    weighted_vectors[loc_details_cols] *= weights["location_details"]

    return cosine_similarity(weighted_vectors)