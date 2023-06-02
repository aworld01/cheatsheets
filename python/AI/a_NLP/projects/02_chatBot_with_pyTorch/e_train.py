import json
from a_tokenize_utils import tokenize
from d_ignore import ignore
from c_bag_of_words import bag_of_words
from model import neuralNet

with open("training.json", "r") as rf:
    data = json.load(rf)
    # print(data)

all_words = []
tags = []
xy = []
for intent in data["intents"]:
    # print(intent)

    tag = intent["tag"]
    # print(tag)

    tags.append(tag) #to add into tags

    for pattern in intent["patterns"]:
        # print(pattern)

        w = tokenize(pattern)
        # print(w)

        all_words.extend(w)

        xy.append((w, tag))

all_words = ignore(all_words) #to ignore special charectors
all_words = sorted(set(all_words)) #to sorted all the words and remove duplicate
tags = sorted(set(tags))

x_train = []
y_train = []

for (pattern_sentence, tag) in xy:

    bag = bag_of_words(pattern_sentence, all_words)
    # print(bag)
    x_train.append(bag)

    label = tags.index(tag)
    # print(label)

    y_train.append(label)
    # print(y_train)

# print(tags)
# print(all_words)
# print(xy)


"""converting into numpy"""
import numpy as np

x_train = np.array(x_train)
y_train = np.array(y_train)

# print(x_train)
# print(y_train)


import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train
        
        """dataset[index]"""
        def __getitem__(self, index):
            return self.x_data[index], self.y_data[index]
        
        def __len__(self):
            return self.n_samples

"""Hyperparameters"""
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(x_train[0])
learning_rate = 0.001
num_epochs = 1000

print(input_size, len(all_words))

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=2)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = neuralNet(input_size, hidden_size, output_size).to(device=device)

"""loss and optimizer"""
criterian = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)

        """forward"""
        outputs = model(words)
        loss = criterian(outputs, labels)

        """backward and optimizer step"""
        optimizer.zero_grad()
        loss.backword()
        optimizer.step()
    
    if (epoch +1) % 100 == 0:
        print(f"Epoch {epoch+1}/{num_epochs}, loss={loss.item():.4f}")
print(f"Final loss, los=(loss.item():.4f)")