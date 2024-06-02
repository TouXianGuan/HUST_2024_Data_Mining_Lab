import numpy as np

def pagerank_complex(M, eps, beta):
    r = np.ones(1000) / 1000
    iter_cnt = 0
    A = beta * M + (1 - beta) * np.ones((1000, 1000)) / 1000
    while True:
        r_new = np.dot(A, r)
        r_new /= np.sum(r_new)
        err = np.sqrt(np.sum(np.square(r_new - r)))
        if err < eps:
            break
        r = r_new.copy()
        iter_cnt += 1
    return r_new, iter_cnt, err