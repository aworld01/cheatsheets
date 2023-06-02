"""
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")
nltk.download("omw-1.4") #if any errors occurs
"""

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
lemmatizer = WordNetLemmatizer()

words1 = ["run", "running", "ran", "runs", "easily", "fairly", "Abdul"]
string = "Narendra Modi has a devoted Following"

"""exampl1"""
# for word in words1:
#     print(f"{word} => {lemmatizer.lemmatize(word, pos=wordnet.VERB)}")


"""example2"""
# words_and_tags = nltk.pos_tag(words1)
# print(words_and_tags)


"""example3"""
def get_pos(tag):
    if tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN
    
print(string)
string = string.split()
words_and_tags = nltk.pos_tag(string)
for word, tag in words_and_tags:
    lemma = f"{lemmatizer.lemmatize(word, pos=get_pos(tag))}"
    print(lemma, end=" ")