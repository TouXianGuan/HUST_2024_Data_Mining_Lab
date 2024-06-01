import os
import time
import threading
from map import create_map_threads
from combine import combine_function
from shuffle import shuffle_function
from reduce import reduce_function, output_results

if __name__ == "__main__":
    start_time = time.time()

    words_set = set(open('../data/words.txt', 'r').read().split())
    map_threads = create_map_threads(words_set)
    for t in map_threads:
        t.join()
    
    finish_time = time.time()
    print("MapReduce time: %.3f s." % (finish_time - start_time))
