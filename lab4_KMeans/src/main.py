import json
import numpy as np
from process import read_data, select_data, norm_data

if __name__ == "__main__":
    anime_data = read_data('../data/anime.csv')
    with open('../tmp/anime_data.json', 'w') as file:
        file.write(json.dumps(anime_data, indent=4))

    K_data = select_data(anime_data)
    with open('../tmp/K_data.json', 'w') as file:
        file.write(json.dumps(K_data.tolist(), indent=4))

    norm_K = norm_data(K_data)
    with open('../tmp/norm_K.json', 'w') as file:
        file.write(json.dumps(norm_K.tolist(), indent=4))
