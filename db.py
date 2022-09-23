import sqlite3

def create_conn(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def main():
    database = "spotify.db"
    create_artist_table = """ CREATE TABLE IF NOT EXISTS artist (
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


    create_album_table = """ CREATE TABLE IF NOT EXISTS album (
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
    create_track_table = """ CREATE TABLE IF NOT EXISTS track (
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

    create_track_feature_table = """ CREATE TABLE IF NOT EXISTS track_feature (
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
    conn = create_conn(database)

    if conn is not None:
        create_table(conn, create_album_table)
        create_table(conn, create_artist_table)
        create_table(conn, create_track_table)
        create_table(conn, create_track_feature_table)
    else:
        print("Error! Cannot create the db connection.")


if __name__ == '__main__':
    main()



def insert_artist(conn, artist):
    insert_artist = '''
                INSERT INTO artist(artist_name, 
                external_url, genre, image_url, followers,
                popularity, type, artist_uri)
                values (?,?,?,?,?,?,?,?)
                '''
    cur = conn.cursor()
    cur.execute(insert_artist, artist)
    conn.commit()
    return cur.lastrowid
    
def insert_album(conn, album):
    insert_album ='''
                INSERT INTO album(album_name, external_url,
                image_url, release_date, total_tracks,
                type, album_uri, artist_uri)
                values(?,?,?,?,?,?,?,?)
                '''
    cur = conn.cursor()
    cur.execute(insert_album, album)
    conn.commit()
    return cur.lastrowid

def insert_track(conn, track):
    insert_track ='''
                INSERT INTO track(song_name, external_url,
                duration_ms, explicit, disc_number, type,
                song_uri, album_id)
                values(?,?,?,?,?,?,?,?)
                '''
    cur = conn.cursor()
    cur.execute(insert_track, track)
    conn.commit()
    return cur.lastrowid

def insert_track_feature(conn, track_feature):
        
    insert_track_feature = '''
                        INSERT INTO track_feature(danceability,
                        energy, instrumentalness, liveness,
                        loudness, speechiness, tempo, type, valence,
                        song_uri)
                        values(?,?,?,?,?,?,?,?,?,?)
                        '''
    cur = conn.cursor()
    cur.execute(insert_track_feature, track_feature)
    conn.commit()
    return cur.lastrowid