import numpy as np
import pandas as pd
from process import read_data, read_tfdif
from user_based import UserBasedRecommendSystem
from content_based import ContentBasedRecommendSystem

if __name__ == "__main__":
    train_data = read_data('../data/train_set.csv')
    test_data = pd.read_csv('../data/test_set.csv')

    used_based_recommender = UserBasedRecommendSystem(train_data)
    pred_ratings = np.zeros(len(test_data))
    for i in range(len(test_data)):
        pred_ratings[i] = used_based_recommender.predict(
            test_data['user_id'][i], test_data['anime_id'][i])
        
    sse = np.sum(np.square(pred_ratings - test_data['rating'].values))
    print("基于用户的协同过滤推荐系统 SSE = ", sse)

    user_id = input('请输入当前用户的id：')
    used_based_recommender.recommend(user_id, 100, 10)

    animes = pd.read_csv('../data/anime.csv')
    animes_tfidf_matrix = read_tfdif(animes)
    
    content_based_recommender = ContentBasedRecommendSystem(
        train_data, animes, animes_tfidf_matrix
    )
    pred_ratings = np.zeros(len(test_data))
    for i in range(len(test_data)):
        pred_ratings[i] = content_based_recommender.predict(
            test_data['user_id'][i], test_data['anime_id'][i])
        
    sse = np.sum(np.square(pred_ratings - test_data['rating'].values))
    print("基于内容的推荐系统 SSE = ", sse)

    user_id = input('请输入当前用户的id：')
    content_based_recommender.recommend(user_id, 100)