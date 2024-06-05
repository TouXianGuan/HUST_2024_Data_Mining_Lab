import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommendSystem(object):
    def __init__(self, utility_mat, animes, tfidf_matrix):
        self.utility_mat = utility_mat
        self.animes = animes
        self.tfidf_mat = tfidf_matrix
        self.index_to_id = dict(enumerate(self.animes['Anime_id']))
        self.id_to_index = dict(zip(self.index_to_id.values(), self.index_to_id.keys()))
        self.anime_sim_mat = cosine_similarity(self.tfidf_mat)

    def predict_score(self, rated, anime_id):
        rated_score = np.array(rated.values) 
        rated_id = np.array(rated.index).astype(int)
        distances = self.anime_sim_mat[anime_id]
        
        computed_dict = {}
        for i in range(len(rated_id)):
            cosine = distances[self.id_to_index[rated_id[i]]]
            if cosine > 0:
                computed_dict[i] = cosine
        if len(computed_dict.keys()):
            score_sum, sim_sum = 0, 0
            for k, v in computed_dict.items():
                score_sum += rated_score[k] * v
                sim_sum += v
            return score_sum / sim_sum
        else:
            return np.mean(rated_score)

    def predict(self, user_id, anime_id):
        user_id = str(user_id)
        
        exist_rating = (self.utility_mat[user_id] != 0)
        rated = self.utility_mat[user_id][exist_rating]
        return self.predict_score(
            rated,  
            self.id_to_index[anime_id]
        )

    def recommend(self, user_id, k):
        user_id = str(user_id)
        
        exist_rating = (self.utility_mat[user_id] != 0)
        rated = self.utility_mat[user_id][exist_rating]
        rated_id = np.array(rated.index).astype(int)
        rec_animes = {}
        for i in range(len(self.animes)):
            idx = self.animes['Anime_id'][i]
            title = self.animes['Name'][i]
            if idx not in rated_id:
                rec_animes[(idx, title)] = self.predict_score(
                   rated, self.id_to_index[idx])
       
        rec_animes_items = list(rec_animes.items())
        rec_animes_items.sort(key=lambda x: x[1], reverse=True)
        rec_animes = [(key, value) for key, value in rec_animes_items][:k]
        
        with open('../result/content_based_recommend.txt', 'w') as file:
            file.write("{}:".format(user_id))
            for item in rec_animes:
                file.write("%-10s\t%-40s\t%.3f" % (item[0][0], item[0][1], item[1]))