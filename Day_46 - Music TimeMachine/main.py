from spotify import Spotify
from billboard import BillBoard

billboard = BillBoard()
top_songs = billboard.get_top_songs()

spotify = Spotify()
playlist_id = spotify.create_playlist(playlist_name=f'{top_songs['date']} Top 10 BillBoard Playlist')

song_items = [ spotify.search_track(track=item[0], artist=item[1]) for idx, item in enumerate(top_songs['titles']) if spotify.search_track(track=item[0], artist=item[1])]

spotify.add_playlist_song(playlist_id=playlist_id, track_uri_list=song_items)





# todo: search and return single title
# for title in titles:
#     spotify.add_track_to_playlist(playlist_id, title)




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
