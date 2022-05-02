## basic code(Hindi)
# import os
# from gtts import gTTS

# def speak(text):
#    tts = gTTS(text=text, lang='hi')
#    filename = 'audios/'+text+'.mp3'
#    tts.save(filename)
       
# data='मेरा नाम एलेक्सा है'
# speak(data)




## basic code(English)
# import os
# from gtts import gTTS

# def speak(text):
#    data=text.lower()
#    tts = gTTS(text=data, lang='en-in')
#    filename = 'audios/'+data+'.mp3'
#    tts.save(filename)
       
# data='My NAMe Is AleXa'
# speak(data)
    
    




##Final
import os
from gtts import gTTS
from playsound import playsound

def speak(text):
   data = text.lower()
   tts = gTTS(text=data, lang='en-in')
   filename = 'audios/'+data+'.mp3'
   if os.path.exists(filename):
       playsound(filename)
   else:
       tts.save(filename)
       playsound(filename)
       
if(__name__=='__main__'):
   data='My NAMe Is AleXa'
   speak(data)