import numpy as np

def generate_center(data, k):
    n = data.shape[1]
    centers = np.zeros((k, n))
    for i in range(n):
        mini = min(data[:, i])
        maxi = max(data[:, i])
        centers[:, i] = mini + float(maxi - mini) * np.random.rand(k)

    return centers

def Euclidean_distance(a, b):
    return np.linalg.norm(a - b)

def distance_sum(data, k):
    distances = np.zeros(k)
    for i in range(180):
        distances[int(data[i, 1]) - 1] += data[i, 0]

    return sum(distances)

def get_acc(data, k):
    clusters = np.zeros((k, k))
    for i in range(180):
        idx2 = int(data[i, 1]) - 1
        idx1 = 0 if i < 60 else 1 if i < 130 else 2
        clusters[idx1][idx2] += 1
    acc = np.sum(np.max(clusters, axis=0)).squeeze()
    acc /= 180
    return acc

def kmeans(data, k, centers):
    Flag = True
    min_data = np.mat(np.zeros((180, 2)))
    for i in range(0, 100):
        if(Flag == False):
            break
        Flag = False
        for j in range(180):
            min_distance = float(1000000)
            min_center = 0
            for p in range(k):
                distance = Euclidean_distance(centers[p], data[j])
                if distance < min_distance:
                    min_distance = distance
                    min_center = p + 1
            if min_data[j, 0] != min_distance or (min_data[j, 1] != min_center and min_center != 0):
                min_data[j, 0] = min_distance
                min_data[j, 1] = min_center
                Flag = True
        for j in range(k):
            point = []
            for p in range(180):
                if min_data[p, 1] == j + 1:
                    point.append(data[p])
            centers[j, :] = np.mean(point, axis=0)
    
    return min_data, centers