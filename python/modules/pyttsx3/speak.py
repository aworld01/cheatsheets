# pip install pyttsx3
import pyttsx3

# pyttsx3.speak("hello sir")

# engine=pyttsx3.init('sapi5')
# voices=engine.getProperty('voices') #to get list of voices
# print(voices) #to print voices
# voice=engine.getProperty('voices')[2].id #to get full details about any specific voice.
# print(voice)




def speak(audio):
    print("  ")
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voice', voices[2].id)
    engine.say(audio)
    engine.runAndWait()

input="hello how are you"

if __name__=="__main__":
    if "hello how are you" in input:
        speak("I'm fine sir")