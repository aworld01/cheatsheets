from tkinter import*

class Window:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Widget")
        """calling function"""
        self.text()
        self.insert()
    def text(self):
        self.txt = Text(self.master)
        self.txt.pack(expand=1, fill=BOTH)
    def insert(self):
        self.img = PhotoImage(file="icon.png")
        self.txt.image_create(END, image = self.img)

if __name__ == "__main__":
    root = Tk()
    obj = Window(root)
    root.mainloop()