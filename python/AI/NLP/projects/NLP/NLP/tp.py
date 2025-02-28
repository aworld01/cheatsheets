import nltk #pip install nltk
# nltk.download('punkt_tab')
from nltk.stem.porter import PorterStemmer

def tokenize(arg):
    return nltk.word_tokenize(arg)

def stem(tok):
    s = PorterStemmer()
    return s.stem(tok.lower())

if __name__=="__main__":
    doc = "This is an apple and the apple is red"
    t = tokenize(doc)
    print(t)
    
    st = [stem(w) for w in t]
    print(st)