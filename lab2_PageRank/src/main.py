import numpy as np
from process import read_data, create_matrix

if __name__ == "__main__":
    data = read_data('../data/data')

    M = create_matrix(data)
    
    with open('../tmp/M.csv', 'w', encoding='utf-8') as f:
        np.savetxt(f, M, fmt='%d', delimiter=',')