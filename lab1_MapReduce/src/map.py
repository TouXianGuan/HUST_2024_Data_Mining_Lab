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

def mapper(folder_index, words_set):
    word_counts = defaultdict(int)
    folder_path = os.path.join('../data', f'folder_{folder_index}')
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            content = extract_words_from_file(file_path)
            output_file = os.path.join('../tmp/map_output', f'map_{folder_index}.txt')
            with open(output_file, 'a', encoding='utf-8') as output:
                for word in content:
                    if word in words_set:
                        output.write("{},{}\n".format(word, 1))        

def create_map_threads(words_set):
    threads = []
    for i in range(1, 10):
        t = threading.Thread(target=mapper, args=(i, words_set))
        threads.append(t)
        t.start()
    return threads