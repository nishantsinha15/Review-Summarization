import gzip
import time
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
start_time = 0


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
        a[int(unit['overall'])].append(unit['reviewText'])
    end_timer()
    print("Time Taken")

read_file()
get_data_ratings()
