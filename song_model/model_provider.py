# import gensim 
# import logging
# import csv

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# songs = []

# # read csv
# with open('../data/songdata.csv') as csvfile:
#    readCSV = csv.reader(csvfile, delimiter=',')
#    for i, row in enumerate(readCSV):
#        preprocessed = gensim.utils.simple_preprocess(str(row))
#        songs.append(preprocessed)

# # train model
# model = gensim.models.Word2Vec (songs, size=400, window=4, min_count=2, workers=10)
# model.train(songs,total_examples=len(songs),epochs=10)

# # load model
# # model = gensim.models.Word2Vec.load("songs_size400_window4_mincount2.model")

# # save model
# model.save("songs_size400_window4_mincount2.model")

# print(model.wv.most_similar(positive=["depressed", "bad"]))


import gensim 
import logging
import csv

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
songs = []
titles = []
authors = []



with open('songdata.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(readCSV):
        preprocessed = gensim.utils.simple_preprocess(str(row[3]))
        songs.append(gensim.models.doc2vec.TaggedDocument(preprocessed, [i]))
        titles.append(row[0] + " - " + row[1])


model = gensim.models.doc2vec.Doc2Vec (vector_size=50, min_count=2, epochs=25, workers=10)
model.build_vocab(songs)

%time model.train(songs, total_examples=model.corpus_count, epochs=model.epochs)

vec = ["depressed", "bad"]
#vec = ["good", "nice", "happy"]
#vec = ["exited", "happy"]
inferred_vector = model.infer_vector(vec)
model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs)) # indexes of most similar songs are generated

print(title[0])


# titles[index]
# songs[index].words

model.save("d2v_vectorsize50_window5_mincount2_epochs15")