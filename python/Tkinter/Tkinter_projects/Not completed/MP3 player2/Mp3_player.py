import os
import pickle
from tkinter import*
from pygame import mixer

font1 = ("times new roman", 15, "bold")

class Player(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Musicxy MP3 Player")
        self.pack()

        """global_variables"""
        self.playlist = []

        """calling methods"""
        self.create_frames()
        self.track_widgets()
        self.control_widgets()
        self.tracklist_widgets()

    def create_frames(self):
        self.track = LabelFrame(self, text="Song Track", font=font1, bg="gray", fg="white", bd=5, relief=GROOVE, width=410, height=300)
        self.track.grid(row=0, column=0)

        self.track_list = LabelFrame(self, text=f"Playlist - {len(self.playlist)}", font=font1, bg="gray", fg="white", bd=5, relief=GROOVE, width=190, height=400)
        self.track_list.grid(row=0, column=1, rowspan=3, pady=5)

        self.controls = LabelFrame(self, font=font1, bg="white", fg="white", bd=5, relief=GROOVE, width=410, height=80)
        self.controls.grid(row=2, column=0, pady=5, padx=10)

    def track_widgets(self):
        pass

    def control_widgets(self):
        pass

    def tracklist_widgets(self):
        pass

        """Initialize Pygame Mixer"""
        mixer.init()

if __name__ == "__main__":
    root = Tk()
    obj = Player(root)
    root.mainloop()

"""16:20 / 1:18:54"""