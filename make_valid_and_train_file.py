import sys, os
import pandas as pd
import string
from nltk.corpus import stopwords
from textblob import Word

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'song_recommender.settings')

import django
django.setup()



if __name__ == "__main__":

    filepath = 'data/songdata.csv'
    songs_df = pd.read_csv(filepath)
    songs_ds = songs_df.sample(frac = 1)
    #print(songs_ds)

    filepath_train = 'data/traindata.csv'
    filepath_valid = 'data/validdata.csv'


    train = songs_ds.head(1000)
    lyrics = train.loc[:, 'text']
    stop = stopwords.words('english')
    lyrics = lyrics.apply(lambda x: ' '.join(x.lower() for x in x.split()))
    lyrics = lyrics.apply(lambda x: ' '.join(x for x in x.split() if x not in string.punctuation))
    lyrics = lyrics.str.replace('[^\w\s]', '')
    lyrics = lyrics.apply(lambda x: ' '.join(x for x in x.split() if not x.isdigit()))
    lyrics = lyrics.apply(lambda x: ' '.join(x for x in x.split() if not x in stop))
    lyrics = lyrics.apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

    valid = songs_ds.tail(200)
    # print(valid)

    train.to_csv(filepath_train)
    valid.to_csv(filepath_valid)
    print('Create files: '+filepath_train + ' and ' + filepath_valid)
