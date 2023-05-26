import numpy as np
import json
import torch
import torch.nn as nn
from torch.utils.data import dataset, dataloader
from b_neuralNetwork import bag_of_words, tokenize, stem
from a_brain import neuralNet

"""load data"""
with open("c_intents.json", "r") as rf:
    intents = json.load(rf)

all_words = []
tags = []
xy = []

for intent in intents["intents"]:
    # print(intent)
    tag = intent["tag"]
    tags.append(tag)
    for pattern in intent["patterns"]:
        # print(pattern)
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = [",", "?", "/", ".","!"]
all_words = [stem(w) for w in all_words if w not in ignore_words] #to ignore special charector
all_words = sorted(set(all_words))

if __name__=="__main__":
    pass
    # print(tags)
    # print(all_words)
    # print(xy)
    print(all_words)