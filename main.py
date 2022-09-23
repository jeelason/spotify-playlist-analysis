import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
import db #(create_conn,insert_album, #insert_artist, insert_track, insert_track_feature)
import sqlite3
from dotenv import load_dotenv

load_dotenv()

database = "spotify.db"
con = sqlite3.connect("spotify.db")



lz_uri = "spotify:artist:36QJpDe2go2KgaRleHCDTp"

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())


results = spotify.search(q='genre', limit=20, type='artist', market='US')
items = results['artists']['items']
for i in items:
    if len(items) > 0:
        print(i['name'])

   
