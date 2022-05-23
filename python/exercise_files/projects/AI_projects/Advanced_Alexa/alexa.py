import os
from listen import listen
from speak import speak
from wish_me import wishMe
from wiki import wiki
from youtube import youtube
from pykit import pyk
from website import website
from whats import whats
from screen import src
from playm import play
from webopen import open
from whats import whats

wishMe()

while True:
    query=listen()
    if "how are you" in query:
        speak("I'm fine sir")
    elif "who are you" in query:
        speak("I'm a computer program my name is alexa")
    elif "what is your name" in query:
        speak("My name is alexa, you can call me computer sir")
    elif "how old are you" in query:
        speak("I'm 18 years old now sir")
    elif "where are you from" in query:
        speak("I'm from India sir")
    elif "who is your boss" in query:
        speak("Abdul Zoha sir is my boss")
    elif "i love you" in query:
        speak("It's my luck that you love me sir, I love you too")
    elif "will you marry me" in query:
        speak("I'm a computer program so how can i marry you sir")
    
    elif "wikipedia" in query:
        wiki(query)
    elif "youtube search" in query:
        youtube(query)
    elif "google search" in query:
        pyk(query)
    elif "open website" in query:
        website(query)
    elif "check aadhar" in query:
        open()
    elif "send whatsapp" in query:
        whats(query)

    # elif "open chromium" in query:
    #     os.startfile("/usr/bin/chromium %U")
    elif "play music" in query:
        play()


    elif "clear the terminal" in query:
        speak("OK sir, I am clear the terminal")
        os.system("clear")
    elif "you need a break" in query:
        speak("ok sir, you can call me anytime")
        os.system("clear")
        break 
    elif "goodbye" in query:
        speak("shuting down, goodbye sir")
        os.system("shutdown now")