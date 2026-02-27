"""fetch file data"""
with open("test_file.txt", "r") as rf:
    data = rf.read()
    # print(data)

"""tokenizetion"""
from nltk.tokenize import sent_tokenize as st

token = st(data)
print(token)