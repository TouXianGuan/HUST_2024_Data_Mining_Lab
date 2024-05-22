from collections import defaultdict

def shuffle_function(combined_results):
    shuffled_data = defaultdict(list)
    for result in combined_results:
        for (word, title), count in result.items():
            shuffled_data[word].append(((word, title), count))
    return shuffled_data