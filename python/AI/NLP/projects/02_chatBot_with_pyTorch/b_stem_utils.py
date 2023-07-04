from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
def stem(word):
    return stemmer.stem(word)


if __name__ == "__main__":
    words1 = ["Organize", "orgnizes", "organizing"]
    words2 = ["go", "goes", "went", "gone", "going"]
    print(words1)

    """example1"""
    # for w in words2:
    #     stemmed_words = stem(w)
    #     print(stemmed_words)

    """example2"""
    stemmed_words = [stem(w) for w in words1]
    print(stemmed_words)