import gensim
import pandas as pd
import string
from nltk.corpus import stopwords
from textblob import Word
import operator


def find_song_suggestions(keywords):
    model = gensim.models.Word2Vec.load("song_model/songs_size400_window4_mincount2.model")
    keywords = list(keywords)
    most_similar_word = model.wv.most_similar(positive=keywords)[0][0]
    keywords.append(most_similar_word)
    filepath = 'data/songdata.csv'
    songs_df = pd.read_csv(filepath).head(1000)
    lyrics = songs_df.loc[:, 'text']

    # clear song text
    stop = stopwords.words('english')
    lyrics = lyrics.apply(lambda x: ' '.join(x.lower() for x in x.split()))
    lyrics = lyrics.apply(lambda x: ' '.join(x for x in x.split() if x not in string.punctuation))
    lyrics = lyrics.str.replace('[^\w\s]', '')
    lyrics = lyrics.apply(lambda x: ' '.join(x for x in x.split() if not x.isdigit()))
    lyrics = lyrics.apply(lambda x: ' '.join(x for x in x.split() if not x in stop))
    lyrics = lyrics.apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    lyrics = lyrics.apply(lambda x: x.split())

    occurrences = {}

    for i, l in lyrics.items():
        occurrences[i] = 0
        for k in keywords:
            occurrences[i] += l.count(k)

    song_id = max(occurrences.items(), key=operator.itemgetter(1))[0]

    return songs_df.loc[song_id, 'artist':'song'].to_dict()
