import json
import numpy as np
from process import read_data, select_data, norm_data
from kmeans import generate_center, kmeans, distance_sum, get_acc

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
    
    centers = generate_center(norm_K, 3)
    with open('../tmp/centers.json', 'w') as file:
        file.write(json.dumps(centers.tolist(), indent=4))

    result_data, result_centers = kmeans(norm_K, 3, centers)
    with open('../result/result_data.json', 'w') as file:
        file.write(json.dumps(result_data.tolist(), indent=4))
    with open('../result/result_centers.json', 'w') as file:
        file.write(json.dumps(result_centers.tolist(), indent=4))

    data_distance_sum = distance_sum(result_data, 3)
    data_acc = get_acc(result_data, 3)
    with open('../result/distance_sum_And_acc.txt', 'w') as file:
        file.write(str(data_distance_sum) + '\n')
        file.write(str(data_acc))
    