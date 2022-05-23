import webbrowser
from speak2 import speak
from listen import listen

def open():
    speak("OK sir, this is what I found for your Search")
    webbrowser.open("https://uidai.gov.in/")
    speak("Done sir")
if __name__ == "__main__":
    query=listen()
    if "check aadhar" in query:
        open()