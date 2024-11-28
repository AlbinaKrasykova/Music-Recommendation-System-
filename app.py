import pandas as pd
import streamlit as st
import requests
from recom_sys import recommend_songs, similarity_matrix, df, get_full_track_artist
from fetch import client_id, client_secret
import requests
import base64


# Spotify API Helper Functions
def fetch_album_images(track_id_list, client_id, client_secret):
    """
    Fetch album images for a list of track IDs from Spotify API.
    """
    # Get access token for Spotify API
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")
    
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(token_url, headers=headers, data=data)
    if response.status_code != 200:
        print(f"Failed to get access token: {response.status_code}, {response.text}")
        return []

    access_token = response.json().get("access_token")

    # Set headers for track details request
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    img_url_list = []
    for track_id in track_id_list:
        url = f"https://api.spotify.com/v1/tracks/{track_id}"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            track_data = response.json()
            album_images = track_data.get("album", {}).get("images", [])
            if album_images:
                img_url_list.append(album_images[0]["url"])  # Get the first image (largest size)
            else:
                img_url_list.append(None)
        else:
            img_url_list.append(None)
    
    return img_url_list

# Load your dataset
df = pd.read_csv('dataset.csv')
df = df.sample(n=10000, random_state=42).reset_index(drop=True)
print(df)

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
selected_song = st.selectbox("Type or select a song from the dropdown", movie_list)
# Get the ID of the selected song
selected_song_id = df.loc[df['track_name'] == selected_song, 'track_id'].values[0]

# Button for showing recommendations
if st.button('Show Recommendation'):
    recommended_tracks, artists, track_id_list = recommend_songs(selected_song, similarity_matrix, df, top_n=5)
    
    # Fetch album images for the recommended tracks
    img_url_list = fetch_album_images(track_id_list, client_id, client_secret)
    
    # Display recommended tracks
    st.write("Recommended Tracks:")
    full_list = get_full_track_artist(recommended_tracks, artists)
    
    # Iterate through recommended tracks and display their details
    for i, track_info in enumerate(full_list):
        st.write(f"### {track_info}")
        
        # Display the album image (if available)
        if img_url_list[i]:
            st.image(img_url_list[i], caption=f"Album Cover for {recommended_tracks[i]}", use_container_width=True)
        else:
            st.write("No album image found.")
