import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os, json

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
    
    def search_track(self, track: str, artist: str):
       search_result = self.sp.search(q=f'track:{track} artist:{artist}',limit=1,type='track')
       if search_result['tracks']['total'] > 0:
            file_path = os.path.join(os.path.dirname(__file__), 'track_results.json')
            # with open(file_path, mode='w') as file:
            #     json.dump(search_result, file, indent=4)
            return search_result['tracks']['items'][0]['uri']
       else:
           return None
    
    def add_playlist_song(self, playlist_id: int, track_uri_list:list):
        result = self.sp.playlist_add_items(playlist_id=playlist_id, items=track_uri_list)
        file_path = os.path.join(os.path.dirname(__file__), 'add_playlist_results.json')
        # with open(file_path, mode='w') as file:
        #     json.dump(result, file, indent=4)
        return True
        
    
    


# spotify = Spotify()

# # playlist_id = spotify.create_playlist(playlist_name='random-test-playlist')
# playlist_id = '5aaE9t53x0AgPX5Pfe73lt'
# print(playlist_id)
# # track_uri = spotify.search_track(track='Standing Next To You', artist='Jung Kook')
# track = 'Heart Of A Woman'
# artist = 'Summer Walker'

# track_uri = spotify.search_track(track=track, artist=artist)
# # search_result = spotify.sp.search(q=f'track:{track} author:{artist}',limit=1,type='track')

# print(track_uri)
# # if track_uri:
# #     result = spotify.add_playlist_song(playlist_id=playlist_id, track_uris=[track_uri])
# #     print(result)


# result = spotify.add_playlist_song(playlist_id=playlist_id, track_uri_list=[track_uri])
# # "uri": "spotify:track:0bYg9bo50gSsH3LtXe2SQn"
# print(result)




