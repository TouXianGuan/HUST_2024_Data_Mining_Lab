import os
import time
import shutil
from map import create_map_threads
from combine import create_combine_threads
from shuffle import create_shuffle_threads
from reduce import reduce_start

if __name__ == "__main__":
    start_time = time.time()
    
    if os.path.exists('../tmp'):
        shutil.rmtree('../tmp')
    os.makedirs('../tmp')
    os.makedirs('../tmp/map_output')
    os.makedirs('../tmp/combine_output')
    os.makedirs('../tmp/shuffle_output')
    os.makedirs('../tmp/reduce_output')
    if os.path.exists('../result'):
        shutil.rmtree('../result')
    os.makedirs('../result')

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
    
    shuffle_threads = create_shuffle_threads()
    for t in shuffle_threads:
        t.join()
    shuffle_finish_time = time.time()
    print("shuffle time: %.3f s." % (shuffle_finish_time - combine_finish_time))

    reduce_start()
    reduce_finish_time = time.time()
    print("reduce time: %.3f s." % (reduce_finish_time - shuffle_finish_time))


    finish_time = time.time()
    print("MapReduce time: %.3f s." % (finish_time - start_time))
