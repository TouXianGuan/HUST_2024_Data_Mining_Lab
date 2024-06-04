import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def read_data(filename):
    train_file = open(filename, 'r', encoding='utf-8')
    train_data = {}
    for line in train_file.readlines()[1:]:
        line = line.strip().split(',')
        if line[0] not in train_data.keys():
            train_data[line[0]] = {line[1]: line[2]}
        else:
            train_data[line[0]][line[1]] = line[2]

    utility_mat = pd.DataFrame(train_data).fillna(0).astype(float)
    return utility_mat


def read_tfdif(animes):
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(animes['Genres'].tolist()).toarray()
    return tfidf_matrix

