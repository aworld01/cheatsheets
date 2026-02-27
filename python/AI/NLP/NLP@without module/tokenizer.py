import re

def reader(arg):
    with open(arg, "r") as rf:
        return rf.read()
data = reader("test.txt")

def sen_tokenizer(arg):
    pattern = r"[.,?!]"
    data = re.split(pattern, arg)
    data.remove("")
    newData = []
    for i in data:
        data = i.lstrip().lower()
        newData.append(data)
    return newData
data2 = sen_tokenizer(data)

def word_tokenizer(arg):
    token = []
    for i in arg:
        token.append(i.split())
    return token
data3 = word_tokenizer(data2)

def word_tokenizer2(arg):
    sentences = []
    for sentence in arg:
        sentences.append(sentence)
    return sentences
data4 = word_tokenizer2(data2)

def allWords(arg):
    words = []
    for i in arg:
        words.extend(i)
    words = sorted(set(words))
    return words
data5 = allWords(data3)

if __name__ == "__main__":
    print(data)
    print()

    print(data2)
    print()

    print(data3)
    print()

    print(data4)
    print()

    print(data5)