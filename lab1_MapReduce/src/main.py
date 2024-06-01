import os
import time
import threading
from map import create_map_threads
from combine import combine_function
from shuffle import shuffle_function
from reduce import reduce_function, output_results

if __name__ == "__main__":
    words_set = set(open('../data/words.txt', 'r').read().split())
    map_output = '../tmp/map_output'
    map_threads = create_map_threads(words_set, map_output)
    for t in map_threads:
        t.join()
