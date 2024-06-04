import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class UserBasedRecommendSystem(object):
    def __init__(self, utility_mat):
        self.utility_mat = utility_mat
        self.user_sim_mat = self.utility_mat.corr()
        with open('../tmp/user_sim_mat.json', 'w') as file:
            json.dump(self.user_sim_mat.to_json(), file)


    def top_k(self, user_id, k):
        user_id = str(user_id)
        sim_dict = dict(self.user_sim_mat[user_id])
        sorted_sim_dict = sorted(sim_dict.items(), key=lambda x: x[1], reverse=True)

        top_k_id = [sorted_sim_dict[i][0] for i in range(k)]
        top_k_mat = self.utility_mat[top_k_id]

        return top_k_mat

    def predict(self, user_id, anime_id, k = 110):
        top_k_mat = self.top_k(user_id, k)
        anime_id = str(anime_id)
        scores = top_k_mat.loc[anime_id]

        return np.mean(scores[scores != 0])

    def recommend(self, user_id, k, n):
        top_k_mat = self.top_k(user_id, k)

        preds = {}
        for i in range(len(self.utility_mat)):
            x = top_k_mat.iloc[i]
            if len(x[x != 0]) > 20: 
                pred_i = np.mean(x[x != 0])
                preds[i] = 0 if np.isnan(pred_i) else pred_i
            else:
               preds[i] = 0
        
        sorted_pred_dict = sorted(
            preds.items(), key=lambda d: d[1], reverse=True)
        
        pred_res = sorted_pred_dict[:min(n, len(sorted_pred_dict))]
        
        with open('../result/user_based_recommend.txt', 'w') as file:
            file.write("{}:".format(user_id))
            for i in range(n):
                idx, score = pred_res[i]
                file.write("%-6s\t%.8f" % (str(self.utility_mat.index[idx]), score))