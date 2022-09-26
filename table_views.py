from db import conn
from prettytable import from_db_cursor


cur = conn.cursor()

    #--------VIEWS---------

'''delete view? 
cur.execute("DROP VIEW v_songs_by_followers")
'''

#1 Top songs by artist in terms of duration_ms
def top_songs_by_time():
    songs_by_time = """
                    CREATE VIEW v_songs_by_time                        
                    AS
                    SELECT track.song_name, track.duration_ms, album.album_name, artist.artist_name
                        FROM track
                        INNER JOIN album                        
                        ON (track.album_id = album.album_id)
                        INNER JOIN artist
                        ON (album.artist_id = artist.artist_id)
                        ORDER by track.duration_ms DESC;                                                
                                    
                  """

    cur.execute(songs_by_time)
    # cur.execute('SELECT * FROM v_songs_by_time')  
    # x = from_db_cursor(cur)
    # print(x)


#2 Top artists in the database by # of followers
def top_artist_by_followers():
    artists_by_followers = """
                         CREATE VIEW v_top_artist_by_followers
                         AS                 
                         SELECT artist_name, popularity, followers
                         FROM artist
                         ORDER BY followers DESC;
                     """
    cur.execute(artists_by_followers)
    # cur.execute('SELECT * FROM v_top_artist_by_followers')  
    # x = from_db_cursor(cur)

#3 Top songs by artist in terms of tempo
def top_songs_by_tempo():
    songs_by_tempo= """
                    CREATE VIEW v_songs_by_tempo
                    AS    
                    SELECT track.song_name, tf.tempo, artist.artist_name
                        FROM track
                        INNER JOIN album                        
                        ON (track.album_id = album.album_id)
                        INNER JOIN track_feature tf
                        on (tf.song_uri = track.song_uri)
                        INNER JOIN artist
                        ON (album.artist_id = artist.artist_id)
                        ORDER by tf.tempo DESC                                                                                     
                  """
    cur.execute(songs_by_tempo)
    # cur.execute('SELECT * FROM v_songs_by_tempo')  
    # x = from_db_cursor(cur)
    # print(x)

#4 see overview of features scatter per artist
def song_features_for_artist():
        features_for_artist= """
                    CREATE VIEW v_features_for_artist
                    AS    
                    SELECT track.song_name, artist.artist_name, tf.danceability, tf.energy, tf.tempo,
                        tf.instrumentalness, tf.liveness, tf.loudness, tf.speechiness, tf.valence
                        FROM track
                        INNER JOIN album a                       
                        ON (track.album_id = a.album_id)
                        INNER JOIN track_feature tf
                        on (tf.song_uri = track.song_uri)
                        INNER JOIN artist
                        ON (a.artist_id = artist.artist_id)
                        ORDER by artist.artist_name ASC;           
                                                                                      
                  """
        cur.execute(features_for_artist)
        # cur.execute('SELECT * FROM v_features_for_artist')  
        # x = from_db_cursor(cur)
        # print(x)

def avg_audio_features_by_artist():
    cur.execute("DROP VIEW IF EXISTS v_avg_audio_features_by_artist;")
    create_view = """
        CREATE VIEW IF NOT EXISTS v_avg_audio_features_by_artist
        AS
        SELECT
            AVG(f.danceability) danceability,
            AVG(f.energy) energy,
            AVG(f.instrumentalness) instrumentalness, 
            AVG(f.liveness) liveness,
            AVG(f.speechiness) speechiness,
            AVG(f.valence) valence 
        FROM artist a
        JOIN album alb
            ON a.artist_id = alb.artist_id 
        JOIN track t
            ON t.album_id = alb.album_id
        JOIN track_feature f 
            ON f.track_id = t.track_id
        GROUP BY a.artist_id
    """

    cur.execute(create_view)
    # cur.execute('SELECT * FROM avg_audio_features_by_artist')  
    # x = from_db_cursor(cur)
    # print(x)



def main():
    top_songs_by_time()
    top_artist_by_followers()
    top_songs_by_tempo()
    song_features_for_artist()
    avg_audio_features_by_artist()



# if __name__ == "__main__":
#     main()