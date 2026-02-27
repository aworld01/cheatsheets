from tkinter import*

class After:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("After method")

        """Label"""
        self.lbl = Label(self.root, text="This is some black color...")
        self.lbl.pack()

        """Button"""
        self.btn = Button(self.root, text="Change color", command=lambda: self.root.after(3000, self.update))
        self.btn.pack()

    def update(self):
        self.lbl.config(fg="red")

if __name__ == "__main__":
    root = Tk()
    obj = After(root)
    root.mainloop()