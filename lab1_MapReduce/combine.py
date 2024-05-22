from collections import defaultdict

def combine_function(word_counts):
    combined_counts = defaultdict(int)
    for (title, word), count in word_counts.items():
        combined_counts[(word, title)] += count
    return combined_counts