import os
import threading

def reducer(folder_index):
    shuffle_output_path = os.path.join('../tmp/shuffle_output', f'shuffle_{folder_index}')
    shuffle_output = open(shuffle_output_path, 'r', encoding='utf-8')

    reduce_output_path = os.path.join('../tmp/reduce_output', f'reduce_{folder_index}')
    reduce_output = open(reduce_output_path, 'w', encoding='utf-8')
    count_dict = {}

    for line in shuffle_output:
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
        reduce_output.write("{},{}\n".format(k, v))

    shuffle_output.close()
    reduce_output.close()

def create_reduce_threads():
    threads = []
    for i in range(1, 4):
        t = threading.Thread(target=reducer, args=(i, ))
        threads.append(t)
        t.start()
    return threads