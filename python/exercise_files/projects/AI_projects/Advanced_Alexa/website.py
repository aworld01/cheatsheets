import webbrowser
from speak2 import speak
from listen import listen


def website(query):
    speak("Tell me the name of the website")
    name=listen()
    web="https://www."+name
    webbrowser.open(web)
    speak("Done sir")
if __name__ == "__main__":
    website("open website")