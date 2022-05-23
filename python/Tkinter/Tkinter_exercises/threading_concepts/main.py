from tkinter import*
from playsound import playsound
from threading import Thread

def screen():
    root = Tk()
    root.mainloop()

def play():
    playsound("nightmare.mp3")

"""creating a thread"""
t=Thread(target=play)
t.daemon = True
t.start()

screen()