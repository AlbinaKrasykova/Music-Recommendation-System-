import requests
import base64

# Function to fetch album images based on track IDs
def fetch_album_images(track_ids, client_id, client_secret):
    # Encode the client_id and client_secret
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    # Get the access token
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
        return  # Exit the function if the token request fails

    # Extract the token
    access_token = response.json().get("access_token")
    print(f"Access Token: {access_token}")

    # Define the headers for the API request
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Iterate through the list of track IDs
    for track_id in track_ids:
        # Spotify API endpoint for track details
        url = f"https://api.spotify.com/v1/tracks/{track_id}"

        # Make the API request
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to fetch track details for {track_id}: {response.status_code}, {response.text}")
            continue  # Skip this track and proceed to the next one

        # Parse the track data
        track_data = response.json()

        # Get the album images from the track's album
        album_images = track_data.get("album", {}).get("images", [])

        if not album_images:
            print(f"No images found for the track {track_id}.")
        else:
            print(f"Album images for track {track_id}:")
            for i, image in enumerate(album_images, start=1):
                print(f"Image {i} URL: {image['url']}")

# Example usage
client_id = "f42bac2a903240178a59ede81d2c***"
client_secret = "a8df94e6e1474b8fa217cc4c8612****"
track_ids = [
    "7qiZfU4dY1lWllzX7mPBI3",  # Example: "Shape of You" by Ed Sheeran
    "3n3Ppam7vgaVa1iaRUc9Lp",  # Example: "Blinding Lights" by The Weeknd
    # Add more track IDs as needed
]

fetch_album_images(track_ids, client_id, client_secret)
