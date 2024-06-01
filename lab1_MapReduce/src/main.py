import os
import threading
from map import create_map_threads
from combine import combine_function
from shuffle import shuffle_function
from reduce import reduce_function, output_results

words_set = set(open('../data/words.txt', 'r').read().split())
map_output_file = '../tmp/map_output'
map_threads = create_map_threads(words_set, map_output_file)
for t in map_threads:
    t.join()
'''
with open(map_output_file, 'r', encoding='utf-8') as in_file:
    lines = in_file.readlines()
word_counts = {}
for line in lines:
    parts = line.strip().split(',')
    if len(parts) == 3:  # 确保每一行有三个部分
        word, count = parts
        word_counts[word] = int(count)

combined_results = [combine_function(result) for result in map_results]
shuffled_data = shuffle_function(combined_results)
reduced_result = reduce_function(shuffled_data)
top_1000_words = sorted(reduced_result.items(), key=lambda x: x[1], reverse=True)[:1000]
output_results(top_1000_words)
'''