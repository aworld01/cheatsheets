# pip install speechrecognition

import speech_recognition as sr
from speaker import speak

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       print("Listing......")
       r.pause_threshold=1
       audio=r.listen(source,timeout=2,phrase_time_limit=5)
    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language="en-in")
        print(f'Your command: {query}\n')
    except:
        return ""
    return query.lower()

if __name__ == "__main__":
    while True:
        data=listen()
        if "how are you" in data:
            speak("I'm fine sir")
        elif "stop" in data:
            break