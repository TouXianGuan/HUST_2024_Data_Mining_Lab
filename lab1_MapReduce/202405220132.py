import threading
from collections import defaultdict

# 定义Map函数
def map_function(folder_index, words_set):
    word_counts = defaultdict(int)
    for filename in os.listdir(f'folder_{folder_index}'):
        with open(f'folder_{folder_index}/{filename}', 'r', encoding='utf-8') as file:
            content = file.read()
            for word in words_set:
                if word in content:
                    word_counts[(filename, word)] += content.count(word)
    return word_counts

# 创建多个线程模拟Map节点
threads = []
for i in range(1, 10):
    t = threading.Thread(target=map_function, args=(i, set(open('words.txt', 'r').read().split())))
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

# 定义Combine函数
def combine_function(word_counts):
    combined_counts = defaultdict(int)
    for (title, word), count in word_counts.items():
        combined_counts[(word, title)] += count
    return combined_counts

# 对每个map节点的输出进行Combine
combined_results = []
for i in range(9):
    combined_results.append(combine_function(results[i]))

    # 定义Shuffle函数
def shuffle_function(combined_results):
    shuffled_data = defaultdict(list)
    for result in combined_results:
        for (word, title), count in result.items():
            shuffled_data[word].append(((word, title), count))
    return shuffled_data

# 执行Shuffle
shuffled_data = shuffle_function(combined_results)

# 定义Reduce函数
def reduce_function(shuffled_data):
    word_totals = defaultdict(int)
    for word, entries in shuffled_data.items():
        for (title, word), count in entries:
            word_totals[word] += count
    return word_totals

# 执行Reduce并输出结果
reduced_result = reduce_function(shuffled_data)
top_1000_words = sorted(reduced_result.items(), key=lambda x: x[1], reverse=True)[:1000]

# 输出结果
with open('reduce_result.txt', 'w') as file:
    for word, count in top_1000_words:
        file.write(f'{word}: {count}\n')