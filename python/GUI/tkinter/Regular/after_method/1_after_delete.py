from tkinter import*
import sys

class After:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("After method")

        """calling method"""
        self.root.after(5000, self.shut) #time to execute(mili-seconds), function

    def shut(self):
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = Tk()
    obj = After(root)
    root.mainloop()