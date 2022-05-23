"""pip install pywhatkit"""
import pywhatkit as pykit
from speak2 import speak

def pyk(query):
    speak("OK sir, this is what I found for your Search")
    query=query.replace("alexa","")
    query=query.replace("google search","")
    pykit.search(query)
    speak("Done sir")
if __name__ == "__main__":
    pyk("what is the age of salman khan")