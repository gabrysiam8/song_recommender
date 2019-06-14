import gensim 
import logging
import csv

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
songs = []

# read csv
with open('songdata.csv') as csvfile:
   readCSV = csv.reader(csvfile, delimiter=',')
   for i, row in enumerate(readCSV):
       preprocessed = gensim.utils.simple_preprocess(str(row))
       songs.append(preprocessed)

# train model
model = gensim.models.Word2Vec (songs, size=400, window=4, min_count=2, workers=10)
model.train(songs,total_examples=len(songs),epochs=10)

# load model
# model = gensim.models.Word2Vec.load("songs_size400_window4_mincount2.model")

# save model
model.save("songs_size400_window4_mincount2.model")

print(model.wv.most_similar(positive=["depressed", "bad"]))