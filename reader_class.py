import gzip
import time

import spacy


class Reader:

    def __init__(self, name = 'reviews_Electronics_5.json.gz'):
        self.name = name

    def read_file(self):
        dataset = []
        data = gzip.open(self.name, 'r')
        for unit in data:
            dataset.append(eval(unit))
        print("Data read successfully")
        return dataset

    def pre_process(self, data = ["Nishant is a fucking piece of meatball"]):
        nlp = spacy.load('en')
        i = 0
        for unit in data:
            review = unit['reviewText'].lower()
            #Add spellchek here
            review = nlp(review)
            if i % 100 == 0:
                print(i)
            i+=1
            # for token in review:
            #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            #           token.shape_, token.is_alpha, token.is_stop)
            unit['reviewText'] = review
        return data

    def read(self):
        data = self.read_file()
        return self.pre_process(data)
    

start = time.time()
read =  Reader()
dataset = read.read()
print("Pre processing took ", start - time.time())
print(dataset[0:2])
