import spacy #pip install spacy, (python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

words = nlp(u"run running ran runs easily fairly")
words1 = ["run", "running", "ran", "runs", "easily", "fairly"]
words2 = ["generous", "generation", "generously", "generate"]
words3 = ["Change", "Changes", "Changed", "Changer","Changing"]

"""example1"""
for word in words:
    print(f"{word.text} => {word.pos_} => {word.lemma_}")