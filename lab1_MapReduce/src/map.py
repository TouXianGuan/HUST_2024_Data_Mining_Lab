import os
import re
import threading
from collections import defaultdict

def extract_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # 使用正则表达式提取单词
        words = re.findall(r'\b[a-zA-Z]+\b', content)
        return words

def map_function(folder_index, words_set, output_path):
    word_counts = defaultdict(int)
    folder_path = os.path.join('../data', f'folder_{folder_index}')
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            content = extract_words_from_file(file_path)
            output_file = os.path.join(output_path, f'map_{folder_index}.txt')
            #output_file = output_path.replace('\\', '/')
            with open(output_file, 'a', encoding='utf-8') as output:
                for word in content:
                    if word in words_set:
                        output.write("{},{}\n".format(word, 1))        

def create_map_threads(words_set, output_file):
    threads = []
    for i in range(1, 10):
        t = threading.Thread(target=map_function, args=(i, words_set, output_file))
        threads.append(t)
        t.start()
    return threads