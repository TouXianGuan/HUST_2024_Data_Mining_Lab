import os
import threading
from collections import defaultdict

def combiner(folder_index):
    map_output_path = os.path.join('../tmp/map_output', f'map_{folder_index}')
    map_output = open(map_output_path, 'r', encoding='utf-8')

    combine_output_path = os.path.join('../tmp/combine_output', f'combine_{folder_index}')
    combine_output = open(combine_output_path, 'w', encoding='utf-8')
    count_dict = {}

    for line in map_output:
        line = line.strip()
        word, count = line.split(',', 1)
        try:
            count = int(count)
        except ValueError:
            continue
        if word in count_dict.keys():
            count_dict[word] += count
        else:
            count_dict[word] = count
    
    count_dict = sorted(count_dict.items(), key=lambda x: x[0], reverse=False)
    for k, v in count_dict:
        combine_output.write("{},{}\n".format(k, v))

    map_output.close()
    combine_output.close()

def create_combine_threads():
    threads = []
    for i in range(1, 10):
        t = threading.Thread(target=combiner, args=(i, ))
        threads.append(t)
        t.start()
    return threads