from b_stem_utils import stem
import numpy as np

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for index, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[index] = 1.0

    return bag

if __name__ == "__main__":
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "i", "you", "bye", "thanks", "cool"]
    bag = bag_of_words(sentence, words)
    print(bag)
