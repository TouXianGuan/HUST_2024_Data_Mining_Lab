import os
import heapq

file_paths = {
    'reduce_1': '../tmp/reduce_output/reduce_1',
    'reduce_2': '../tmp/reduce_output/reduce_2',
    'reduce_3': '../tmp/reduce_output/reduce_3'
}

# 读取文件并合并数据
def result():
    data = {}
    for key, path in file_paths.items():
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    word, count = line.strip().split(',', 1)
                    data[word] = data.get(word, 0) + int(count)
    top1000(data)


def top1000(data):
    top_words = heapq.nlargest(1000, data.items(), key=lambda item: item[1])
    with open('../result/result.csv', 'w', encoding='utf-8') as result_file:
        for word, count in top_words:
            result_file.write(f"{word},{count}\n")