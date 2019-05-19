import sys, os
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'song_recommender.settings')

import django
django.setup()

from recommender.models import Song


def save_song_from_row(song_row):
    song = Song()
    song.artist = song_row[0]
    song.title = song_row[1]
    song.link = song_row[2]
    song.text = song_row[3]
    song.save()


if __name__ == "__main__":

    filepath = 'data/songdata.csv'
    print('Reading from file '+filepath)
    songs_df = pd.read_csv(filepath)
    print(songs_df)

    songs_df.apply(
        save_song_from_row,
        axis=1
    )
