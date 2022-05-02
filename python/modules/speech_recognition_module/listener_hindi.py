# pip install speechrecognition

import speech_recognition as sr
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       print("listing......")
       r.pause_threshold=1
       audio=r.listen(source,timeout=2,phrase_time_limit=5)
    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language="hi")
        print(f'Your command: {query}\n')
    except:
        return ""
    return query.lower()

if __name__ == "__main__":
    while True:
        data=listen()
        if 'रुको' in data:
            break