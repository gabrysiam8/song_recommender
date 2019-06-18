import gensim
import logging
import csv

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
songs = []
titles = []
authors = []


with open('../data/songdata.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(readCSV):
        preprocessed = gensim.utils.simple_preprocess(str(row[3]))
        songs.append(gensim.models.doc2vec.TaggedDocument(preprocessed, [i]))
        titles.append(row[0] + " - " + row[1])


model = gensim.models.doc2vec.Doc2Vec (vector_size=50, min_count=2, epochs=25, workers=10)
model.build_vocab(songs)

model.train(songs, total_examples=model.corpus_count, epochs=model.epochs)

model.save("d2v_vectorsize50_window5_mincount2_epochs15")