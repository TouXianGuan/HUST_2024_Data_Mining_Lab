import os
import time
import threading
from map import create_map_threads
from combine import create_combine_threads
from shuffle import shuffle_function
from reduce import reduce_function, output_results

if __name__ == "__main__":
    start_time = time.time()

    words_set = set(open('../data/words.txt', 'r').read().split())

    map_threads = create_map_threads(words_set)
    for t in map_threads:
        t.join()
    map_finish_time = time.time()
    print("map time: %.3f s." % (map_finish_time - start_time))

    combine_threads = create_combine_threads()
    for t in combine_threads:
        t.join()
    combine_finish_time = time.time()
    print("combine time: %.3f s." % (combine_finish_time - map_finish_time))
    
    finish_time = time.time()
    print("MapReduce time: %.3f s." % (finish_time - start_time))
