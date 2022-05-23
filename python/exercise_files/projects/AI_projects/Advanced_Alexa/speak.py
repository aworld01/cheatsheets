import os
from gtts import gTTS
from playsound import playsound

def speak(text):
   data = text.lower()
   tts = gTTS(text=data)
   filename = 'audios/'+data+'.mp3'
   if os.path.exists(filename):
       playsound(filename)
   else:
       tts.save(filename)
       playsound(filename)
       
if(__name__=='__main__'):
   speak("नमस्ते सर आप कैसे हो")