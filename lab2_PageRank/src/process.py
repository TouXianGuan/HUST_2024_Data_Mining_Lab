import numpy as np

def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    data = []
    for line in lines:
        line = line.strip()
        word, value = line.split(': ')
        titles = value.replace('\'','').strip("{}").split(',')

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

def matrix_normalization(matrix):
    ones_count = np.sum(matrix, axis=0)
    norm_matrix = np.zeros_like(matrix)
    non_zero_columns = ones_count != 0
    norm_matrix[:, non_zero_columns] = matrix[:, non_zero_columns] / ones_count[non_zero_columns]
    
    return norm_matrix