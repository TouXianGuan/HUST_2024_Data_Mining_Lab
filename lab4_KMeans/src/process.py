import csv
import numpy as np

def read_data(filename):
    data = []
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader) 

        for row in reader:
            popularity = int(row[4])
            if row[5] == 'Unknown' or row[5] == '':
                score_10 = 0
            else:
                score_10 = int(row[5])
            if row[6] == 'Unknown' or row[6] == '':
                score_9 = 0
            else:
                score_9 = int(row[6])
            if row[7] == 'Unknown' or row[7] == '':
                score_8 = 0
            else:
                score_8 = int(row[7])
            if row[8] == 'Unknown' or row[8] == '':
                score_7 = 0
            else:
                score_7 = int(row[8])
            if row[9] == 'Unknown' or row[9] == '':
                score_6 = 0
            else:
                score_6 = int(row[9])
            if row[10] == 'Unknown' or row[10] == '':
                score_5 = 0
            else:
                score_5 = int(row[10])
            if row[11] == 'Unknown' or row[11] == '':
                score_4 = 0
            else:
                score_4 = int(row[11])
            if row[12] == 'Unknown' or row[12] == '':
                score_3 = 0
            else:
                score_3 = int(row[12])
            if row[13] == 'Unknown' or row[13] == '':
                score_2 = 0
            else:
                score_2 = int(row[13])
            
            data.append([popularity, score_10, score_9, score_8, score_7, score_6, score_5, score_4, score_3, score_2])

    return data

def select_data(data):
    sorted_data = sorted(data, key=lambda x: x[0], reverse=True)
    third = len(sorted_data) // 3
    
    high_data = sorted_data[0:60]
    for item in high_data:
        item.append(1)
    middle_data = sorted_data[third:third+60]
    for item in middle_data:
        item.append(2)
    low_data = sorted_data[2*third:2*third+60]
    for item in low_data:
        item.append(3)
    
    return np.matrix(np.array(high_data + middle_data + low_data))

def norm_data(data):
    column_sums = np.amax(data, axis=0)
    norm_data = data / column_sums

    return norm_data