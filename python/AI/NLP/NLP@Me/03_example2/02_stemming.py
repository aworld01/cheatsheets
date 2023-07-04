import nltk #pip install nltk

words1 = ["run", "running", "ran", "runs", "easily", "fairly"]
words2 = ["generous", "generation", "generously", "generate"]
words3 = ["Change", "Changes", "Changed", "Changer","Changing"]

"""example1"""
# from nltk.stem.porter import PorterStemmer
# Stemmer = PorterStemmer()

# for word in words1:
#     print(f"{word} => {Stemmer.stem(word)}")


"""exampl2"""
from nltk.stem.snowball import SnowballStemmer
Stemmer = SnowballStemmer(language="english")

for word in words1:
    print(f"{word} => {Stemmer.stem(word)}")