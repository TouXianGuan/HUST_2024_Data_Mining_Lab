import json
from process import read_data

if __name__ == "__main__":
    anime_data = read_data('../data/anime.csv')
    with open('../tmp/anime_data.json', 'w') as file:
        file.write(json.dumps(anime_data, indent=4))