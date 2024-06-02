import os
import threading
from collections import defaultdict

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
    
    reduce_output = open('../tmp/reduce_output/reduce', 'w', encoding='utf-8')    
    for word, (total_count, titles) in result.items():
        reduce_output.write(f"{word}, ({', '.join(titles.keys())}), {total_count}\n")

    word_counts = [(word, count) for word, (count, titles) in result.items()]
    word_counts.sort(key=lambda x: x[1], reverse=True)
    top_1000_words = [word for word, count in word_counts[:1000]]

    top_1000 = defaultdict(lambda: [{},0])
    for word, (count, titles) in result.items():
        if word in top_1000_words:
            titles_list = list(titles.keys()) if isinstance(titles, dict) else titles
            top_1000[word] = ([title for title in titles_list if title in top_1000_words], count)

    sorted_top_1000 = sorted(top_1000.items(), key=lambda x: x[1][1], reverse=True)
    result_file = open('../result/result', 'w', encoding='utf-8')    
    for word, (titles, count) in sorted_top_1000:
        result_file.write(f"{word}, ({', '.join(titles)}), {count}\n")