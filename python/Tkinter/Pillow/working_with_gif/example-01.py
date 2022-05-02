from tkinter import*
from PIL import Image, ImageTk, ImageSequence
import time

class Animate:
    def __init__(self, root):
        self.root = root
        self.root.title("Animation")
        self.root.geometry("600x400")

        """Label"""
        self.lbl = Label(self.root, bg="white")
        self.lbl.pack()

        """Buttons"""
        start = Button(self.root, text="Start", command=self.start)
        start.pack()

        stop = Button(self.root, text="Stop", command=self.stop)
        stop.pack()
        
    def start(self):
        file = "cortana.gif"
        image = Image.open(file)
        n = image.n_frames #to get no of frames of gif
        for item in ImageSequence.Iterator(image):
            img = item.resize((300, 300), Image.ANTIALIAS)
            img2 = ImageTk.PhotoImage(img)
            self.lbl.config(image=img2)
            self.root.update()
            time.sleep(0.02)
            print(img2)
        self.a=self.root.after(0, self.start)
    def stop(self):
        self.root.after_cancel(self.a)

if __name__ == "__main__":
    root = Tk()
    win = Animate(root)
    root.mainloop()