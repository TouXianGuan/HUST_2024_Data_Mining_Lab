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
    combine_output_path = os.path.join('../tmp/combine_output', f'combine_{folder_index}')
    combine_output = open(combine_output_path, 'r', encoding='utf-8')

    shuffle_output1_path = os.path.join('../tmp/shuffle_output', f'shuffle_1')
    shuffle_output1 = open(shuffle_output1_path, 'a', encoding='utf-8')
    shuffle_output2_path = os.path.join('../tmp/shuffle_output', f'shuffle_2')
    shuffle_output2 = open(shuffle_output2_path, 'a', encoding='utf-8')
    shuffle_output3_path = os.path.join('../tmp/shuffle_output', f'shuffle_3')
    shuffle_output3 = open(shuffle_output3_path, 'a', encoding='utf-8')

    for line in combine_output:
        line = line.strip()
        title, word, count = line.split(',')
        idx = word_grouping(word[0])
        if idx == 1:
            shuffle_output1.write("{},{},{}\n".format(title, word, count))
        elif idx == 2:
            shuffle_output2.write("{},{},{}\n".format(title, word, count))
        else:
            shuffle_output3.write("{},{},{}\n".format(title, word, count))
    
    combine_output.close()
    shuffle_output1.close()
    shuffle_output2.close()
    shuffle_output3.close()

def create_shuffle_threads():
    threads = []
    for i in range(1, 10):
        t = threading.Thread(target=shuffler, args=(i, ))
        threads.append(t)
        t.start()
    return threads
