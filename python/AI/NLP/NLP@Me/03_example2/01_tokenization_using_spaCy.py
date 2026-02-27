import spacy
nlp = spacy.load("en_core_web_sm")

string = "We're here to help! Send snail-mail, email fahad@gmail.com or visit us at https://fahadhussaincs.blogspot.com/!"
doc = nlp(string) #to convert into tokens

"""check datatype"""
# print(f"{string} => {type(string)}")
# print(f"{doc} => {type(doc)}")

"""tokenization"""
"""example1"""
# for token in doc:
#     print(token.text, end=" | ")


"""example2"""
for token in doc:
    print(token.text)