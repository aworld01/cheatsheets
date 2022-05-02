import os
from gtts import gTTS
from playsound import playsound

def speak2(text):
   tts = gTTS(text=text)
   filename = 'audios/default.mp3'
   tts.save(filename)
   playsound(filename)
       
if(__name__=='__main__'):
   data='we have very low power, please connect to charging the system will shutdown very soon'
   speak2(data)