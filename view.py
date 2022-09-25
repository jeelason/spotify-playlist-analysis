# import sqlite3

# conn = sqlite3.connect("spotify.db")
# cur = conn.cursor()

#     #--------VIEWS---------

# def artist_table_view():    
#     artist_view = """ CREATE VIEW v_artists                       
#                       SELECT artist_name,
#                       FROM artist
#                       WHERE artist_name = 'Drake';
#                   """
#     cursor.execute(artist_view)
#     print(conn.execute("SELECT * FROM v_artists").fetchall())

# artist_table_view()
