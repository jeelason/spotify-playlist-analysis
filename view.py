import sqlite3
from db import conn
from prettytable import from_db_cursor


cur = conn.cursor()

    #--------VIEWS---------

'''delete view? 
cur.execute("DROP VIEW v_songs_by_time")
'''

#1 Top songs by artist in terms of duration_ms
#2 Top artists in the database by # of followers
#3 Top songs by artist in terms of tempo

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
                        ORDER by track.duration_ms DESC                                                
                        LIMIT 100;             
                  """

    cur.execute(songs_by_time)
    # cur.execute('SELECT * FROM v_songs_by_time')  
    # x = from_db_cursor(cur)
    # print(x)

def top_songs_by_followers():
    songs_by_followers = """
                         CREATE VIEW v_songs_by_followers
                         AS                 
                         SELECT artist_name, popularity, followers
                         FROM artist
                         ORDER BY followers DESC;
                     """
    cur.execute(songs_by_followers)
    cur.execute('SELECT * FROM v_songs_by_followers')  
    x = from_db_cursor(cur)
    print(x)


# def top_songs_by_tempo():
#     songs_by_tempo= """
#                     SELECT 
#                     """


top_songs_by_time()
# top_songs_by_followers()
