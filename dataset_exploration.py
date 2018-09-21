import gzip
import time
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
start_time = 0


def test():
    s1 = "The car is driven on road"
    s2 = "The truck is driven on highway"

    vectorizer = TfidfVectorizer()
    response = vectorizer.fit_transform([s1, s2])
    print(vectorizer.vocabulary_)
    print(response)


def start_timer():
    global start_time
    start_time = time.time()


def end_timer():
    print("Time Taken = ", time.time() - start_time)


def read_file(name = 'reviews_Electronics_5.json.gz' ):
    dataset = []
    start_timer()
    data = gzip.open(name, 'r')
    for unit in data:
        dataset.append(eval(unit))
    print("Data read successfully")
    end_timer()
    return dataset


def get_data_ratings(dataset):
    a = ['' for i in range(6)]
    start_timer()
    for unit in dataset:
        a[int(unit['overall'])] += ' ' + (unit['reviewText'])
    end_timer()
    for i in a:
        print("Length of ", i, "th = ", len(i))
    return a


def get_tfidf(dataset = ['road is sexy', 'road is uneven', 'road is sexy', 'road is black']):
    vectorizer = TfidfVectorizer()
    response = vectorizer.fit_transform(dataset)
    print(vectorizer.vocabulary_)
    print(response)



def main():
    dataset = read_file()
    dataset = get_data_ratings(dataset)
    # get_tfidf(dataset)


# main()
get_tfidf()