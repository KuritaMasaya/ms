import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
                                               client_secret="",
                                               redirect_uri="",
                                               scope="user-top-read"))

results = sp.current_user_top_tracks(limit=5, offset=0, time_range='medium_term')
for item in enumerate(results['items']):
    print(item)