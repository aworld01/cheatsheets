'''
Speech Recognition based Python packages:
-SpeechRecognition
-google-cloud-speech
-apiai
-pocketsphinx
-assemblyai
-watson-devloper-cloud
-wit

##Install SpeechRecognition
pip install SpeechRecognition

##Import Speech Recognition Package
import speech_recognition as spr

##Validate the installation(check version)
spr.__version__

##to take voice from Audio_file.
import speech_recognition as spr
noisyspeech=spr.AudioFile('noisy_speech.wav')
with noisyspeech as noisesource:
    audio=recog.record(noisesource)
recog.recognize_google(audio)

##to filter noise from Audio_file.
import speech_recognition as spr
noisyspeech=spr.AudioFile('noisy_speech.wav')
with noisyspeech as noisesource:
    recog.adjust_for_ambient_noise(noisesource) #to remove noise from audio.
    audio=recog.record(noisesource)
recog.recognize_google(audio)

##to take voice from Audio_file.
import speech_recognition as spr
noisyspeech=spr.AudioFile('noisy_speech.wav')
with noisyspeech as noisesource:
    audio=recog.record(noisesource)
recog.recognize_google(audio, show_all=True) #to see several possible transcripts form a single audio source.



Convert Speech to Text in Real Time using Microphone (pyaudio required).
mc=spr.Microphone()
mc.list_microphone_names() #to check mics available in your computer.
mc=spr.Microphone(device_index=0) #to select a particular microphone.



'''