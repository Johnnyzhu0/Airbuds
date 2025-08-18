import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

#loads the environment variables from inside .env file
load_dotenv()

#defining the permissions this app is asking for
scope = "user-library-read"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = os.getenv("SPOTIFY_CLIENT_ID"),
    client_passcode = os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_url = os.getenv("SPOTIFY_REDIRECT_URL")
))


