import os
import threading
from collections import defaultdict

def map_function(folder_index, words_set):
    word_counts = defaultdict(int)
    folder_path = os.path.join('../source_data', f'folder_{folder_index}')
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                for word in words_set:
                    if word in content:
                        word_counts[(filename, word)] += content.count(word)
    return word_counts

def create_map_threads(words_set):
    threads = []
    for i in range(1, 10):
        t = threading.Thread(target=map_function, args=(i, words_set))
        threads.append(t)
        t.start()
    return threads