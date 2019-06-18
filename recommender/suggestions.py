import gensim
import csv


def find_song_suggestions(keywords):
    model = gensim.models.doc2vec.Doc2Vec.load("song_model/d2v_vectorsize50_window5_mincount2_epochs15")
    keywords = list(keywords)
    artists = []
    titles = []
    with open('data/songdata.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(readCSV):
            artists.append(row[0])
            titles.append(row[1])

    inferred_vector = model.infer_vector(keywords)
    indexes = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs)) # indexes of most similar songs are generated
    best_index = indexes[0][0]

    best_result = {}
    best_result['artist'] = artists[best_index]
    best_result['song'] = titles[best_index]

    return best_result

