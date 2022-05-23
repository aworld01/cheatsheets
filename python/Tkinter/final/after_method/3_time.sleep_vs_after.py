from tkinter import*
import time

class After:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("After method")

        """after() method example"""
        # print("Before the function call..")
        # root.after(5000, self.update)
        # print("After the function call")

        """time.sleep() method example (this pauses the entire programe)"""
        print("Before the function call..")
        time.sleep(5)
        self.update()
        print("After the function call")

    def update(self):
        print("This is the text in the function")

if __name__ == "__main__":
    root = Tk()
    obj = After(root)
    root.mainloop()