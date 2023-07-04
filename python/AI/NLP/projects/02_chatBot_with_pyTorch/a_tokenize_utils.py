"""
pip install nltk #to install nltk
nltk --version #to check installed nltk version

"""
import nltk
# nltk.download("punkt") #run for first use

def tokenize(sentence):
    return nltk.word_tokenize(sentence)



if __name__ == "__main__":
    string1 = "What would you do with 1000000$?"
    string2 = "aren't you happy with so much money?"

    print(string2)
    print(tokenize(string2))