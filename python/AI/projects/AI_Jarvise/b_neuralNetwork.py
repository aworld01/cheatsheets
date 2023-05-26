"""
neurons.py
"""

import numpy as np #pip install numpy
import nltk #pip install nltk
# nltk.download("punkt") #only for first time after install nltk
from nltk.stem.porter import PorterStemmer

Stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)
def stem(word):
    return Stemmer.stem(word.lower())
def bag_of_words(tokenized_sentence, words):
    sentence_word = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)

    for idx, w in enumerate(words):
        bag[idx] = 1
    return bag




if __name__ == "__main__":
    string = "Hello world! How are you?"
    data = tokenize(string)
    print(data)
    data = stem(data)
    print(data)