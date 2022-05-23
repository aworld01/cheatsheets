import wikipedia #pip install wikipedia
from speak2 import speak

def wiki(query):
    speak("searching wikipedia")
    query=query.replace("wikipidia", "")
    result=wikipedia.summary(query, sentences=2)
    speak("according to wikipedia\n")
    print(result)
    speak(result)
if __name__ == "__main__":
    wiki("who is salman khan")