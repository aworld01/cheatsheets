import webbrowser
from speak2 import speak

def youtube(query):
    speak("OK sir, this is what I found for your Search")
    query=query.replace("alexa", "")
    query=query.replace("youtube search","")
    web='https://www.youtube.com/results?search_query='+query
    webbrowser.open(web)
    speak("Done sir")
if __name__ == "__main__":
    youtube("new hindi songs")