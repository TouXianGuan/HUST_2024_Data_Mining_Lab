def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    data = []
    for line in lines:
        line = line.strip()
        word, value = line.split(': ')
        titles = value.replace('\'','').strip("{}").split(',')

        titles.insert(0, word)
        data.append(titles)

    return data