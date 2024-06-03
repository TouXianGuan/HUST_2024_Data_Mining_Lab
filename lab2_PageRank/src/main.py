import numpy as np
from pagerank import pagerank_complex
from process import read_data, create_matrix, matrix_normalization

if __name__ == "__main__":
    data = read_data('../data/data')

    M = matrix_normalization(create_matrix(data))
    with open('../tmp/M.csv', 'w', encoding='utf-8') as f:
        np.savetxt(f, M, fmt='%.20f', delimiter=',')

    r, iter_cnt, err = pagerank_complex(M, 1e-8, 0.85)
    with open('../result/r.csv', 'w', encoding='utf-8') as f:
        np.savetxt(f, r, fmt='%.20f', delimiter=',')
    with open('../result/iter_cnt', 'w', encoding='utf-8') as f:
        f.write(str(iter_cnt))
    with open('../result/err', 'w', encoding='utf-8') as f:
        f.write(str(err))