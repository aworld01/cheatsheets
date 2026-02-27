from tkinter import*

class Window:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Widget")
        """calling function"""
        self.scroll()

    def scroll(self):
        """Scrollbar"""
        self.srb = Scrollbar(self.master)
        self.srb.pack(side=RIGHT, fill=Y)

        """Text"""
        self.txt = Text(self.master, yscrollcommand=self.srb.set)
        self.txt.pack(expand=1, fill=BOTH)
        
        """Scrollbar configuration"""
        self.srb.config(command=self.txt.yview)
        

if __name__ == "__main__":
    root = Tk()
    obj = Window(root)
    root.mainloop()