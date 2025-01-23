import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os

SPOTIFY_CLIENT_ID= os.environ.get('SPOTIFY_CLIEND_ID')
SPOTIFY_CLIENT_SECRET= os.environ.get('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = 'https://example.com'

class Spotify:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                        client_secret=SPOTIFY_CLIENT_SECRET,
                                                        redirect_uri=REDIRECT_URI,
                                                        scope="user-library-read, playlist-modify-private"))
    def create_playlist(self, playlist_name: str):
        user_id = self.sp.current_user()['id']
        # self.playlist_id = ''
        return self.sp.user_playlist_create(user=user_id, name=playlist_name, public=True, collaborative=True, description='Playlist created from billboards')

    def add_playlist_songs(self, title: str):
        playlist_id = self.create_playlist('Billboard 100 Songs')
        self.sp.playlist_add_items(playlist_id, title, position=None)
        
    def search_tracks(self, titles: list):
        results = []
        for title in titles:
            results.append(sp.search(q=title, limit=1)['tracks']['items'][0])



