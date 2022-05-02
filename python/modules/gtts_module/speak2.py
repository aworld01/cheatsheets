import os
from gtts import gTTS
from playsound import playsound

def speak(text):
   data = text.lower()
#    tts = gTTS(text=data)
   tts = gTTS(text=data, lang='hi')
   filename = 'audios/'+data+'.mp3'
   if os.path.exists(filename):
       playsound(filename)
   else:
       tts.save(filename)
       playsound(filename)
       
if(__name__=='__main__'):
   data='we have very low power, please connect to charging the system will shutdown very soon'
   speak(data)