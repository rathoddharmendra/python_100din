from spotify import Spotify
from billboard import BillBoard

billboard = BillBoard()
top_songs = billboard.get_top_songs()

spotify = Spotify()
playlist_id = spotify.create_playlist(f'{top_songs['date']} Billboard Top 100 ')


# todo: search and return single title
# for title in titles:
#     spotify.add_track_to_playlist(playlist_id, title)