import wikipedia #pip install wikipedia
from default import speak2 as sp
from translate import tran

def wiki(query):
    print("searching wikipedia")
    sp("विकिपीडिया पर खोजा जा रहा है")
    query=query.replace("विकीपीडिया", "")
    result=wikipedia.summary(query, sentences=2)
    txt=tran(result)
    print("according to wikipedia")
    sp("विकिपीडिया के अनुसार")
    print(result)
    sp(txt)
if __name__ == "__main__":
    wiki("who is salman khan")