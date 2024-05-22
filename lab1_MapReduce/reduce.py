from collections import defaultdict

def reduce_function(shuffled_data):
    word_totals = defaultdict(int)
    for word, entries in shuffled_data.items():
        for (title, word), count in entries:
            word_totals[word] += count
    return word_totals

def output_results(top_1000_words):
    with open('reduce_result.txt', 'w') as file:
        for word, count in top_1000_words:
            file.write(f'{word}: {count}\n')