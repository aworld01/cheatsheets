from speak2 import speak
import pywhatkit as pykit
from listen import listen

def whats(query):
    speak("tell me the name of the person")
    name=listen()
    if "roshan tara" in name:
        speak("tell me the message")
        msg=listen()
        speak("tell me the time in hour sir")
        hour=int(listen())
        speak("tell me the minuts")
        minu=int(listen())
        pykit.sendwhatmsg_instantly("+918797217771", msg, hour, minu, 20)
        speak("ok sir, sending whatsapp message")
if __name__ == "__main__":
    data=listen()
    if "send whatsapp" in data:
        whats(data)