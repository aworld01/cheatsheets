from tkinter import*
from pygame import mixer

root = Tk()
root.title("Mp3 Player")
root.geometry("700x400")

"""Global variables"""
playlist = ["Hello", "Hi"]

"""Initialize the Pygame mixer"""
mixer.init()

font1 = ("times new roman", 15, "bold")
main = Frame(root, bg="white")
main.place(x=0, y=0, relwidth=1, relheight=1)

"""creating the frames"""
track = LabelFrame(main, text="Song Track", font=font1, bg="gray", fg="white", relief=GROOVE, width=410, height=358)
track.grid(row=0, column=0, padx=(0, 5))

track_list = LabelFrame(main, text=f"Playlist - {len(playlist)}", font=font1, bg="gray", fg="white", relief=GROOVE, width=290, height=400)
track_list.grid(row=0, column=1, rowspan=2, padx=5)

controls = Frame(main, bg="white", relief=GROOVE)
controls.grid(row=1, column=0)

bw_btn = Button(controls, text="Back").grid(row=0, column=0, padx=5)
fw_btn =  Button(controls, text="Next").grid(row=0, column=1, padx=5)
play_btn =  Button(controls, text="Play").grid(row=0, column=2, padx=5)
pause_btn =  Button(controls, text="Pause").grid(row=0, column=3, padx=5)
stop_btn =  Button(controls, text="Stop").grid(row=0, column=4, padx=5)


root.mainloop()

"""pt1 - 11:40 / 24:54"""