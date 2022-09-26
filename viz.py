import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from db import conn
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})
cur = conn.cursor()

# for row in cur.execute("SELECT name FROM sqlite_master WHERE type='view';"):
#   print(row)

followers = pd.read_sql_query("SELECT * FROM v_top_artist_by_followers", conn)
duration = pd.read_sql_query("SELECT * FROM v_songs_by_time", conn)
features = pd.read_sql_query("SELECT * FROM v_features_for_artist", conn)


# print(features)
	


sns.set_theme()
# sns.distplot(followers,x='followers', hue="artist_name", element="poly")
# sns.barplot(followers, x='artist_name', y="num_followers")
# sns.barplot(followers, x="followers", y='artist_name', palette="pastel")
# sns.pairplot(followers, hue="artist_name", diag_kind="hist")


# pal = dict(Lunch="seagreen", Dinner=".7")
# g = sns.FacetGrid(features, hue="artist_name", palette=pal, height=5)
# g.map(sns.scatterplot, "danceability", "tempo", s=100, alpha=.5)
# g.add_legend()

cols = ["danceability",
"energy",
"instrumentalness",
"liveness",
"loudness",
"speechiness",
"tempo",
"valence"]

# g = sns.PairGrid(features[cols], height=3.5, hue='danceability')
# g.map(sns.scatterplot)

# g.map(plt.scatter, "danceability", "tempo")
# g.map(plt.plot, "danceability", "tempo")


def avg_audio_features_by_artist():
    # plt.figure(figsize=(16,1))
    df = pd.read_sql_query("SELECT * FROM v_avg_audio_features_by_artist", conn)
    g = sns.boxplot(df)
    g.set(ylim=(0,1), title='Average Audio Features by Artist')
    plt.xticks(rotation = 35, rotation_mode='anchor', ha='right')
    
    plt.show()


avg_audio_features_by_artist()