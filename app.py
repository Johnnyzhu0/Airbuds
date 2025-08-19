import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

#loads the environment variables from inside .env file
load_dotenv()

#defining the permissions this app is asking for
scope = "user-library-read"

# Create client with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri = os.getenv("SPOTIFY_REDIRECT_URL")
))

#Test to get current user info
user = sp.current_user()
print(f"Logged in as {user['display_name']}")
print(user['email'])
print(user['followers'])



