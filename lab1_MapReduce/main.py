import os
import threading
from map import create_map_threads

words_set = set(open('../source_data/words.txt', 'r').read().split())
map_threads = create_map_threads(words_set)
for t in map_threads:
    t.join()

'''map_results = []
combined_results = [combine_function(result) for result in map_results]
shuffled_data = shuffle_function(combined_results)
reduced_result = reduce_function(shuffled_data)
top_1000_words = sorted(reduced_result.items(), key=lambda x: x[1], reverse=True)[:1000]
output_results(top_1000_words)'''
