import wikipedia # pip install wikipedia
from default import speak2 as sp

data="salman khan wikipedia"
if 'wikipedia' in data:
    sp("searching wikipedia")
    query=data.replace("wikipedia", "")
    result=wikipedia.summary(query, sentences=2)
    sp("according to wikipedia")
    sp(result)
    print(result)