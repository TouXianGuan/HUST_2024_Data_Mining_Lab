import csv
from process import read_data

if __name__ == "__main__":
    data = read_data('../data/anime.csv')

    with open('../tmp/data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)