import sys, os
import pandas as pd
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'song_recommender.settings')

import django
django.setup()

from recommender.models import Song

if __name__ == "__main__":

    filepath = 'data/songdata.csv'
    songs_df = pd.read_csv(filepath)
    songs_ds = songs_df.sample(frac = 1)
    #print(songs_ds)

    filepath_train = 'data/traindata.csv'
    filepath_valid = 'data/validdata.csv'

    train = songs_ds.head(1000)
    # print(train)

    valid = songs_ds.tail(200)
    # print(valid)

    train.to_csv(filepath_train)
    valid.to_csv(filepath_valid)
    print('Create files: '+filepath_train + ' and ' + filepath_valid)
