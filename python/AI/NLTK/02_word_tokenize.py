"""fetch file data"""
with open("test_file.txt", "r") as rf:
    data = rf.read()


"""tokenizetion"""
from nltk import word_tokenize as wtok1
from nltk import wordpunct_tokenize as wtok2
from nltk import regexp_tokenize as wtok3 #best
from nltk import RegexpTokenizer as wtok4
# from nltk import WordPunctTokenizer as wpt1

token1 = wtok1(data)
token2 = wtok2(data)
token3 = wtok3(data, "[\w']+")

exp = wtok4("[\w']+")
token4 = exp.tokenize(data)

print(token1)
print()
print(token2)
print()
print(token3)
print()
print(token4)