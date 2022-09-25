import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

from db import (
    conn,
    create_artist_table,
    create_album_table,
    create_track_feature_table,
    create_track_table,
)

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())


fav_uri = "spotify:playlist:4v7VBQWmPx6XsoOJaJosWN"


artists_id = []


def insert_artists():
    # artists_id
    artist_name = []
    external_url = []
    genre = []
    image_url = []
    followers = []
    popularity = []
    type = []
    artist_uri = []

    results = spotify.playlist_tracks(fav_uri, limit=20)

    artists = results["items"]
    for i in range(13,20):
        artist_id = artists[i]["track"]["artists"][0]["id"]
        artists_id.append(artist_id)
        artist_name.append(artists[i]["track"]["artists"][0]["name"])
        external_url.append(f"https://open.spotify.com/artist/{artist_id}")

    for artist in artists_id:
        result = spotify.artist(artist)
        genre.append(result["genres"][0])
        image_url.append(result["images"][0]["url"])
        followers.append(result["followers"]["total"])
        popularity.append(result["popularity"])
        type.append(result["type"])
        artist_uri.append(result["uri"])

    artists_dict = {
        "artist_id": artists_id,
        "artist_name": artist_name,
        "external_url": external_url,
        "genre": genre,
        "image_url": image_url,
        "followers": followers,
        "popularity": popularity,
        "type": type,
        "artist_uri": artist_uri,
    }

    artists_df = pd.DataFrame(
        artists_dict,
        columns=[
            "artist_id",
            "artist_name",
            "external_url",
            "genre",
            "image_url",
            "followers",
            "popularity",
            "type",
            "artist_uri",
        ],
    )

    create_artist_table()
    try:
        artists_df.to_sql("artist", conn, if_exists="append", index=False)
        print("artists added")
    except:
        print("Artist data already exists")
    conn.commit()
 


album_id = []


def insert_albums():
    # album_id
    album_name = []
    external_url = []
    image_url = []
    release_date = []
    total_tracks = []
    type = []
    album_uri = []
    art_id = []

    for artist in artists_id:
        results = spotify.artist_albums(
            artist_id=artist, album_type="album", country="US"
        )
        albums = results["items"]
        while results["next"]:
            results = spotify.next(results)
            albums.extend(results["items"])

        for album in albums:
            album_id.append(album["id"])
            album_name.append(album["name"])
            external_url.append(album["external_urls"]["spotify"])
            image_url.append(album["images"][0]["url"])
            release_date.append(album["release_date"])
            total_tracks.append(album["total_tracks"])
            type.append(album["type"])
            album_uri.append(album["uri"])
            art_id.append(album["artists"][0]["id"])

    albums_dict = {
        "album_id": album_id,
        "album_name": album_name,
        "external_url": external_url,
        "image_url": image_url,
        "release_date": release_date,
        "total_tracks": total_tracks,
        "type": type,
        "album_uri": album_uri,
        "artist_id": art_id,
    }

    albums_df = pd.DataFrame(
        albums_dict,
        columns=[
            "album_id",
            "album_name",
            "external_url",
            "image_url",
            "release_date",
            "total_tracks",
            "type",
            "album_uri",
            "artist_id",
        ],
    )

    create_album_table()
    try:
        albums_df.to_sql("album", conn, if_exists="append", index=False)
        print("albums added")
    except:
        print("Album data already exists")
    conn.commit()
    


song_uri = []


def insert_album_tracks():
    track_id = []
    song_name = []
    external_url = []
    duration_ms = []
    explicit = []
    disc_number = []
    type = []
    # song_uri
    alb_id = []

    for album in album_id:
                
        results = spotify.album_tracks(album, market="US")
        songs = results["items"]
        
        for song in songs: 
            track_id.append(song["id"])
            song_name.append(song["name"])
            external_url.append(song["external_urls"]["spotify"])
            duration_ms.append(song["duration_ms"])
            explicit.append(song["explicit"])
            disc_number.append(song["disc_number"])
            type.append(song["type"])
            song_uri.append(song["uri"])
            alb_id.append(album)

    tracks_dict = {
        "track_id": track_id,
        "song_name": song_name,
        "external_url": external_url,
        "duration_ms": duration_ms,
        "explicit": explicit,
        "disc_number": disc_number,
        "type": type,
        "song_uri": song_uri,
        "album_id": alb_id,
    }

    tracks_df = pd.DataFrame(
        tracks_dict,
        columns=[
            "track_id",
            "song_name",
            "external_url",
            "duration_ms",
            "explicit",
            "disc_number",
            "type",
            "song_uri",
            "album_id",
        ],
    )

    create_track_table()
    try:
        tracks_df.to_sql("track", conn, index=False, if_exists="append")
        print("tracks added")
    except:
        print("Track data already exists")

    conn.commit()
    


def insert_track_features():
    track_id = []
    danceability = []
    energy = []
    instrumentalness = []
    liveness = []
    loudness = []
    speechiness = []
    tempo = []
    type = []
    valence = []
    track_uri = []

    for song in song_uri:
        track = spotify.audio_features(tracks=song)
        for track in track:
            track_id.append(track["id"])
            danceability.append(track["danceability"])
            energy.append(track["energy"])
            instrumentalness.append(track["instrumentalness"])
            liveness.append(track["liveness"])
            loudness.append(track["loudness"])
            speechiness.append(track["speechiness"])
            tempo.append(track["tempo"])
            type.append(track["type"])
            valence.append(track["valence"])
            track_uri.append(track["uri"])

    features_dict = {
        "track_id": track_id,
        "danceability": danceability,
        "energy": energy,
        "instrumentalness": instrumentalness,
        "liveness": liveness,
        "loudness": loudness,
        "speechiness": speechiness,
        "tempo": tempo,
        "type": type,
        "valence": valence,
        "song_uri": track_uri,
    }


    features_df = pd.DataFrame(
        features_dict,
        columns=[
            "track_id",
            "danceability",
            "energy",
            "instrumentalness",
            "liveness",
            "loudness",
            "speechiness",
            "tempo",
            "type",
            "valence",
            "song_uri",
        ],
    )

    create_track_feature_table()
    try:
        features_df.to_sql("track_feature", conn, if_exists="append", index=False)
        print("track features added")
    except:
        print("Data already exists")

    conn.commit()
    conn.close()
    print("close successful")


def main():
    insert_artists()
    insert_albums()
    insert_album_tracks()
    insert_track_features()


if __name__ == "__main__":
    main()
