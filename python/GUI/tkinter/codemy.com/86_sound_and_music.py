from tkinter import*
import pygame

"""define a function"""
def play():
    pygame.mixer.init() #to initialize pygame (Must)
    pygame.mixer.music.load("/home/thor/Music/nightmare-90160.mp3")
    # pygame.mixer.music.play() #it will play by loop
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

"""configure main window"""
root = Tk()
root.title("Codemy.com")
root.geometry("500x400")

frm = Frame(root)
frm.pack()

start = Button(frm, text="Play", command=play).grid(row=0, column=0, pady=20)
stop = Button(frm, text="Stop", command=stop).grid(row=0, column=1)
pau = Button(frm, text="pause", command=pause).grid(row=0, column=2)
unpau = Button(frm, text="unpause", command=unpause).grid(row=0, column=3)

root.mainloop()