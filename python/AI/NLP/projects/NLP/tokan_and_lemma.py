import spacy

# !python -m spacy download en_core_web_sm

nlp = spacy.load("en_core_web_sm")

def tokenize(text):
   tok = [token for token in nlp(text)]
   return tok

def lemma(text):
   lemm = [token.lemma_.lower() for token in nlp(text)]
   return lemm

if __name__=="__main__":
   s = "This is a apple and the apple is red."
   tok = tokenize(s)
   print(tok)
   
   lem = lemma(s)
   print(lem)