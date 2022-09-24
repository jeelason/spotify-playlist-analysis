import sqlite3

conn = sqlite3.connect("spotify.db")
cursor = conn.cursor()

def create_artist_table():
    artist_table = """ CREATE TABLE IF NOT EXISTS artist (
                                            artist_id varchar(50) PRIMARY KEY,
                                            artist_name varchar(255),
                                            external_url varchar(100),
                                            genre varchar(100),
                                            image_url varchar(100),
                                            followers int,
                                            popularity int,
                                            type varchar(50),
                                            artist_uri varchar(100)
                                        );"""
    cursor.execute(artist_table)
    conn.commit()

    

def create_album_table():
    album_table = """ CREATE TABLE IF NOT EXISTS album (
                                    album_id varchar(50) PRIMARY KEY,
                                    album_name varchar(255),
                                    external_url varchar(100),
                                    image_url varchar(100),
                                    release_date date,
                                    total_tracks int,
                                    type varchar(50),
                                    album_uri varchar(100),
                                    artist_id varchar(50),
                                    FOREIGN KEY (artist_id) REFERENCES artist (artist_id)
                                );"""
    cursor.execute(album_table)
    conn.commit()

def create_track_table():
    track_table = """ CREATE TABLE IF NOT EXISTS track (
                                        track_id varchar(50) PRIMARY KEY,
                                        song_name varchar(255),
                                        external_url varchar(100),
                                        duration_ms int,
                                        explicit boolean,
                                        disc_number int,
                                        type varchar(50),
                                        song_uri varchar(100),
                                        album_id varchar(50),
                                        FOREIGN KEY (album_id) REFERENCES album (album_id)
                                    );"""
    cursor.execute(track_table)
    conn.commit()

def create_track_feature_table():
    track_feature_table = """ CREATE TABLE IF NOT EXISTS track_feature (
                                        track_id varchar(50) PRIMARY KEY,
                                        danceability double,
                                        energy double,
                                        instrumentalness double,
                                        liveness double,
                                        loudness double,
                                        speechiness double,
                                        tempo double,
                                        type varchar(50),
                                        valence double,
                                        song_uri varchar(100),
                                        FOREIGN KEY (song_uri) REFERENCES track (song_uri)
                                    );"""
    cursor.execute(track_feature_table)
    conn.commit()

def main():
    create_artist_table()
    create_album_table()
    create_track_feature_table()
    create_track_table()


if __name__ == '__main__':
    main()