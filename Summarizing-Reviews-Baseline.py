import gzip


def read_file():
    file_name = 'reviews_Electronics_5.json.gz'
    dataset = []
    data = gzip.open(file_name, 'r')
    for unit in data:
        dataset.append(eval(unit))
    return dataset


def pre_process(data):
    return None


def pos_tagging(tokens):
    return None


def main():
    data = read_file()
    print(data[0])


main()