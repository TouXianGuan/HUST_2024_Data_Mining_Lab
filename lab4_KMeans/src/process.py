import csv
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def read_data(filename):
    with open('../data/anime.csv') as f:
        reader = csv.reader(f)
        next(data)
        for row in data:
            samples.append(row)
    samples = np.array([[float(x) for x in row] for row in samples])

    '''data_sorted = data.sort_values('Popularity', ascending=False)

    third_rows = len(data_sorted) // 3

    # 选择Popularity高、中、低三类，每类选择60个数据
    high_data = data_sorted.head(60)
    mid_data = data_sorted.iloc[third_rows:third_rows+60]
    low_data = data_sorted.iloc[2*third_rows:2*third_rows+60]

    #high_data['K'] = 'High'
    #mid_data['K'] = 'Mid'
    #low_data['K'] = 'Low'

    scaler = MinMaxScaler()
    high_data_normalized = pd.DataFrame(scaler.fit_transform(high_data.drop('K', axis=1)), columns=high_data.columns[:-1])
    mid_data_normalized = pd.DataFrame(scaler.transform(mid_data.drop('K', axis=1)), columns=mid_data.columns[:-1])
    low_data_normalized = pd.DataFrame(scaler.transform(low_data.drop('K', axis=1)), columns=low_data.columns[:-1])

    normalized_data = pd.concat([high_data_normalized, mid_data_normalized, low_data_normalized])
    data = pd.concat([high_data, mid_data, low_data])'''
    return data