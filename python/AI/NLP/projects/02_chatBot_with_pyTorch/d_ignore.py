from b_stem_utils import stem

def ignore(words):
    ignore_words = ["?", ".", ",", "!"]
    return [stem(w) for w in words if w not in ignore_words]






if __name__ == "__main__":
    data = ['Hi', 'Hey', 'How', 'are', 'you', 'Is', 'anyone', 'there', '?', 'Hello', 'Good', 'day', 'Bye', 'See', 'you', 'later', 'Goodbye', 'Tell', 'me', 'a', 'joke', 'Tell', 'me', 'something', 'funny', '!', 'Do', 'you', 'know', 'a', 'joke', '?']
    print(data)
    print()

    data = ignore(data)
    print(data)