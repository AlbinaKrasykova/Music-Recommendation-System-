#!/bin/bash


'''
Path: /Users/albinakrasykova/Desktop/Projects/Music_Recom/Music-Recommendation-System-

+ mv ~/Downloads/dataset.csv . (move datset from downloads to you curr directory)


1. Download the dataset from Kaggle -> https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
2. curr path -> /Users/albinakrasykova/Desktop/Projects/Music_Recom/Music-Recommendation-System-

Recom system steps:

#How can i monitor Ray - ? 





import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import ray

# Initialize Ray
ray.init(ignore_reinit_error=True)

# Load your dataset
df = pd.read_csv('dataset.csv')

#df = df.sample(n=10000, random_state=42)

# Select relevant features for similarity computation
features = df[['liveness', 'valence', 'tempo']]  # Example features

# Function to compute cosine similarity
@ray.remote
def compute_similarity_chunk(features_chunk):
    return cosine_similarity(features_chunk)

# Split features into chunks
feature_chunks = np.array_split(features, 4)  # Split into 4 chunks

# Process each chunk in parallel
similarity_results = ray.get([compute_similarity_chunk.remote(chunk) for chunk in feature_chunks])

# Combine results into the final similarity matrix
full_similarity_matrix = np.concatenate(similarity_results, axis=0)


# Now you can continue with the rest of your recommendation process
print(full_similarity_matrix)

# Shutdown Ray
ray.shutdown()
'''



import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import ray

# Initialize Ray
ray.init(ignore_reinit_error=True)

# Load the dataset (make sure the file exists in your working directory)
df1 = pd.read_csv('dataset.csv')  # Replace with correct file path
df = df1.sample(n=10000, random_state=42)  # Use a smaller subset of 10,000 samples

# Reset the index after sampling
df = df.reset_index(drop=True)  # This will reset the index and drop the old one

print(df.head())

# Select relevant features for similarity computation (e.g., tempo, danceability, energy)
features = df[['tempo', 'danceability', 'energy']]  # Choose more relevant features if needed

# Step 1: Define a Ray remote function to compute the similarity
@ray.remote
def compute_cosine_similarity(features):
    # Compute the cosine similarity matrix
    return cosine_similarity(features)

# Step 2: Use Ray to compute the cosine similarity matrix
similarity_matrix = ray.get(compute_cosine_similarity.remote(features))

# Step 3: Recommendation function for a specific track (using item-based approach)
def recommend_songs(song_name, cosine_sim, df, top_n=5):
    # Ensure the song_name exists in the dataset
    if song_name not in df['track_name'].values:
        raise ValueError(f"Song '{song_name}' not found in dataset.")
    
    # Step 1: Find the index of the selected song based on track_name
    song_index = df[df['track_name'] == song_name].index[0]
    
    # Step 2: Get the similarity scores for the selected song
    similarity_scores = list(enumerate(cosine_sim[song_index]))
    
    # Step 3: Sort the tracks based on similarity scores (highest to lowest) and get top N similar tracks
    sorted_tracks = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # Step 4: Get the indices of the top N similar tracks
    similar_tracks = [x[0] for x in sorted_tracks[1:top_n+1]]  # Skip the first one (itself)
    
       # Step 5: Retrieve details for the similar tracks
    track_names = df.iloc[similar_tracks]['track_name'].tolist()
    artists = df.iloc[similar_tracks]['artists'].tolist()
    track_ids = df.iloc[similar_tracks]['track_id'].tolist()
    
    return track_names, artists, track_ids

# Example: Get recommendations for a specific song by its name
selected_song_name = 'Yellow Submarine'  # Replace with a track name from your dataset

recommended_tracks, artists, _ = recommend_songs(selected_song_name, similarity_matrix, df, top_n=5)

# Display the recommended tracks
print("Recommended Tracks:")

def get_full_track_artist(recommended_tracks, artists):
    return [f"{track} by {artist}" for track, artist in zip(recommended_tracks, artists)]

# Step 6: Shutdown Ray after computation
ray.shutdown()




