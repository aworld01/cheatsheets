"""
pip install spacy
python -m spacy download en_core_web_sm
"""
import spacy
nlp = spacy.load("en_core_web_sm")
from spacy import displacy

string = "I'm with you for the entire life in P.K.!"
# print(string, type(string))

doc = nlp(string)
# print(doc, type(doc))

# for token in doc:
#     print(token.text, end=" | ")



doc2 = nlp(u"We're here to help! Send snail-mail, email fahad@gmail.com or visit us at https://fahadhussaincs.blogspot.com/!")
# print(doc2, type(doc2))

# for t in doc2:
#     print(t)


doc3 = nlp(u"A 5km NYC cab ride costs $10.30")
# for t in doc3:
#     print(t)


doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")
# for t in doc4:
#     print(t)


doc5 = nlp(u"It is better to give than to receive.")
# print(len(doc5)) #to check length.

# print(len(doc5.vocab)) #to check vocab.

# print(doc5[2]) #to get 3rd token.

# print(doc5[2:5]) #Retrieve three tokens from the middle.

# print(doc5[-4:]) #retrieve the last four tokens.



doc6 = nlp(u"Apple to build a Hong Kong factory for $6 million")
# for token in doc6:
#     print(token.text, end=" | ")

# print("\n----")

# print(doc6.ents)

# for ent in doc6.ents:
#     print(f"{ent.text} - {ent.label_} - {spacy.explain(ent.label_)}")

# print(len(doc6.ents)) #to retrieve len of doc.ents



# doc7 = nlp(u"Autonomous cars shift insurance liability toward manufacturers.")
# for token in doc7:
#     print(token, end=" | ")
# print("\n----")
# for chunk in doc7.noun_chunks:
#     print(chunk.text)



doc8 = nlp(u"Apple is going to build a U.K. factory for $6 million.")
displacy.render(doc8, style="dep", jupyter=True, options={"distance": 110})


doc8 = nlp(u"Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million.")
displacy.render(doc8, style="ent", jupyter=True, options={"distance": 110})


doc10 = nlp(u"This is a sentence.")
displacy.serve(doc10, style="dep")