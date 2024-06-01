import os
import threading

def word_grouping(word: str) -> int:
    if 97 <= ord(word) <= 102 or 65 <= ord(word) <= 70:  # a(A) 到 f(F)
        return 1
    elif 103 <= ord(word) <= 112 or 71 <= ord(word) <= 80:  # g(G) 到 p(P)
        return 2
    else:
        return 3


def shuffler(folder_index):
    shuffle_output_path = os.path.join('../tmp/shuffle_output', f'shuffle_{folder_index}')
    shuffle_output = open(shuffle_output_path, 'w', encoding='utf-8')

    for i in range(1, 10):
        combine_output_path = os.path.join('../tmp/combine_output', f'combine_{i}')
        with open(combine_output_path, 'r', encoding='utf-8') as combine_output:
            for line in combine_output:
                line = line.strip()
                title, word, count = line.split(',')
                idx = word_grouping(word[0])
                if idx == folder_index:
                    shuffle_output.write("{},{},{}\n".format(title, word, count))
        combine_output.close()
    
    shuffle_output.close()

def create_shuffle_threads():
    threads = []
    for i in range(1, 4):
        t = threading.Thread(target=shuffler, args=(i, ))
        threads.append(t)
        t.start()
    return threads
