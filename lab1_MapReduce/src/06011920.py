import threading
from collections import defaultdict
from heapq import nlargest

# 定义一个全局字典来存储汇总结果
global_result = defaultdict(lambda: [0, {}])

def process_file(file_path):
    word_dict = defaultdict(int)
    with open(file_path, 'r') as file:
        for line in file:
            title, word, count = line.strip().split(',')
            count = int(count)
            # 更新全局字典
            global_result[word][0] += count
            global_result[word][1][title] = global_result[word][1].get(title, 0) + count

# 创建线程
threads = []
for i in range(3):
    thread = threading.Thread(target=process_file, args=('file' + str(i) + '.txt',))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

# 转换数据结构，以便输出
output_data = [(word, titles, total_count) for word, (total_count, titles) in global_result.items()]

# 输出前1000大的数据
top_1000 = nlargest(1000, output_data, key=lambda x: x[2])

# 打印结果
for word, titles, count in top_1000:
    print(f"{word}, ({', '.join(titles.keys())}), {count}")