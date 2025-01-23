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
                                                        scope="user-library-read, playlist-modify-private, playlist-modify-public"))
    def create_playlist(self, playlist_name: str):
        user_id = self.sp.current_user()['id']
        self.playlist_id = self.sp.user_playlist_create(user=user_id, name=playlist_name, public=True, collaborative=True, description='Playlist created from billboards')['id']
        return self.playlist_id
    
    def add_playlist_song(self, playlist_id: int, title: str):
        return self.sp.playlist_add_items(playlist_id, title, position=None)
        
    
    def search_track(self, title: str):
       return sp.search(q=title, limit=1)['tracks']['items'][0])

    def add_tract_to_playlist(self):
        result = self.search_track()
        try:
            self.add_playlist_songs
        except Exception as e:
            print(f'Error adding track to playlist: {str(e)}')




