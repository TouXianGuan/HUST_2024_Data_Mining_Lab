import os
import threading
from collections import defaultdict
from heapq import nlargest

result = defaultdict(lambda: [0, {}])


def reducer(folder_index):
    shuffle_output_path = os.path.join('../tmp/shuffle_output', f'shuffle_{folder_index}')
    shuffle_output = open(shuffle_output_path, 'r', encoding='utf-8')

    for line in shuffle_output:
        line = line.strip()
        title, word, count = line.split(',')
        try:
            count = int(count)
        except ValueError:
            continue
        result[word][0] += count
        result[word][1][title] = result[word][1].get(title, 0) + count
    shuffle_output.close()

def create_reduce_threads():
    threads = []
    for i in range(1, 4):
        t = threading.Thread(target=reducer, args=(i, ))
        threads.append(t)
        t.start()
    return threads

def reduce_start():
    reduce_threads = create_reduce_threads()
    for t in reduce_threads:
        t.join()
    
    reduce_data = [(word, titles, total_count) for word, (total_count, titles) in result.items()]
    reduce_output = open('../tmp/reduce_output/reduce', 'w', encoding='utf-8')    
    for word, (total_count, titles) in result.items():
        reduce_output.write(f"{word}, ({', '.join(titles.keys())}), {total_count}\n")
    top_1000 = nlargest(1000, reduce_data, key=lambda x: x[2])
    with open('../result/result.csv', 'w') as output_file:
        for word, titles, count in top_1000:
            output_file.write(f"{word}, ({', '.join(titles.keys())}), {count}\n")