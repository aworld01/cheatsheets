import webbrowser
from speak import speak

def wb(query):
    speak("OK sir, this is that I found for your Search")
    query=query.replace("alexa", "")
    query=query.replace("youtube search")