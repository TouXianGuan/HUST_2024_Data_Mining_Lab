import csv
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def read_data(filename):
    data = []
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader) 

        for row in reader:
            popularity = row[4]
            score_10 = row[5]
            score_9 = row[6]
            score_8 = row[7]
            score_7 = row[9]
            score_6 = row[10]
            score_5 = row[11]
            score_4 = row[12]
            score_3 = row[13]
            score_2 = row[14]

            
            data.append([popularity, score_10, score_9, score_8, score_7, score_6, score_5, score_4, score_3, score_2])

    return data