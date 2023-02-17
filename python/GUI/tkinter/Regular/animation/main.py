import time
from tkinter import*
from PIL import Image, ImageTk, ImageSequence

class Animate:
    def __init__(self, root):
        self.root = root
        self.root.title("Animation")
        self.root.geometry("600x400")

        """Labels"""
        self.lbl = Label(self.root)
        self.lbl.place(x=20, y=20)

        """Buttons"""
        Button(self.root, text="Play", command=self.play).place(x=450, y=300)
        Button(self.root, text="Exit", command=self.root.destroy).place(x=500, y=300)
        

    def play(self):
        global img
        file = "v.gif"
        image = Image.open(file)
        for i in ImageSequence.Iterator(image):
            img = i.resize((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.lbl.config(image=img)
            print(img)
            self.root.update()
            time.sleep(0.01)
        self.root.after(0, self.play)
if __name__ == "__main__":
    root = Tk()
    motion = Animate(root)
    root.mainloop()