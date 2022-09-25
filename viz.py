import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from db import conn

cur = conn.cursor()

# for row in cur.execute("SELECT name FROM sqlite_master WHERE type='view';"):
#   print(row)

followers = pd.read_sql_query("SELECT * FROM v_songs_by_followers", conn)
duration = pd.read_sql_query("SELECT * FROM v_songs_by_time", conn)
# print(followers)
	



# sns.set_theme()

# sns.displot(followers,x='followers', hue="artist_name", stat='density')
# sns.barplot(followers, x='artist_name', y="num_followers")
sns.barplot(followers, x="followers", y='artist_name', palette="light:#5D9")
plt.show()

