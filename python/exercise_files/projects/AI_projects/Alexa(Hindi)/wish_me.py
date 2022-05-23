import datetime
from speak import speak

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<17:
        speak("Good afternoon sir!")
    elif hour>=18 and hour<19:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    speak("मेरा नाम एलेक्सा है, मैं आपकी क्या मदद कर सकती हूँ")

if(__name__=='__main__'):
    wishMe()