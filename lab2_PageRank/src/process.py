import numpy as np

def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    data = []
    for line in lines:
        parts = line.strip().split(', ')
        word = parts[0]
        if len(parts) == 3:
            titles = parts[1].replace('(', '').replace(')', '')
        elif len(parts) == 4:
            titles = []
            titles.insert(0, parts[1].replace('(', ''))
            titles.insert(1, parts[2].replace(')', ''))
        else:
            titles = parts[2:-2]
            titles.insert(0, parts[1].replace('(', ''))
            titles.append(parts[-2].replace(')', ''))

        data.append((word, titles))
    
    return data

def create_matrix(data):
    matrix = np.zeros((1000, 1000))
    
    # 填充矩阵
    for i in range(0, 1000):
        for j in range(0, 1000):
            if data[j][0] in data[i][1]:
                matrix[i][j] = 1
    return matrix