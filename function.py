import pandas as pd
import plotly.graph_objects as go
import json
import streamlit as st
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import ray
from recom_sys import recommend_songs, similarity_matrix, df

# Load your dataset
df = pd.read_csv('dataset.csv')
df = df.sample(n=10000, random_state=42).reset_index(drop=True)



# Custom CSS to style the header and background
page_bg_img = f"""
<style>
/* Apply green background to the entire page */
body {{
    background-color: green;
}}


.header-container {{
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}}

.header-container img {{
    height: 40px;  /* Adjust the height of the logo */
    margin-right: 15px;
}}

.header-container h1 {{
    font-size: 2em;
    font-weight: bold;
}}
</style>
"""

# Apply custom background to Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)

# Display the header with the logo next to it
st.markdown(
    """
    <div class="header-container">
        <h1>Spotify Recommendation System</h1>
        <img src="https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg" alt="Spotify Logo">
    </div>
    """, 
    unsafe_allow_html=True
)

# Create dropdown for selecting a track
movie_list = df['track_name'].values
selected_song = st.selectbox("Type or select a movie from the dropdown", movie_list)

# Button for showing recommendations
if st.button('Show Recommendation'):
    recommended_movie_names = recommend_songs(selected_song, similarity_matrix, df, top_n=5)
    st.write("Recommended Tracks:")
    st.write(recommended_movie_names)
