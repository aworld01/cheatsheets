"""
nltk.download("wordnet") #fisrt time use
nltk.download("omw-1.4") #if error occures
nltk.download("averaged_perceptron_tagger") #to check word type on parts of speech

"""
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()

"""example1"""
# lemmatized = lemma.lemmatize("mice")
# print(lemmatized)

"""example2"""
# lemmatized = lemma.lemmatize("going") #considers any word as noun by default
# lemmatized = lemma.lemmatize("going", pos=wordnet.VERB)
# print(lemmatized)

"""example3"""
# nltk.download("averaged_perceptron_tagger") #to check word type on parts of speech

# sentence = ["apple", "going", "hit"]
# pos = nltk.pos_tag(sentence)
# print(pos, type(pos))




"""final"""
def getTag(arg):
    if arg.startswith("J"):
        return wordnet.ADJ
    elif arg.startswith("V"):
        return wordnet.VERB
    elif arg.startswith("N"):
        return wordnet.NOUN
    elif arg.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN
def lemmatizer(tag):
    lemma_word = []
    for word, tag in nltk.pos_tag(tag):
        lem = lemma.lemmatize(word, pos=getTag(tag))
        lemma_word.append(lem)
    return lemma_word
        

if __name__ == "__main__":
    sentence1 = ["go", "went", "gone", "goes", "going"]
    sentence2 = ["drive", "driver"]
    sentence3 = ["do", "did", "done", "does", "doing"]
    sentence4 = "Narendra Modi has a devoted following".split()
    l = lemmatizer(sentence1)
    print(l)