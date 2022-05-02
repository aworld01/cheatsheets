from tkinter import*
"""
self.txt = Text(self.frm, width=50, height=20) #width=50 charectors, height=20 lines

data = self.txt.get(1.0, END) #data = self.txt.get(Line.Index, LastIndex)
data = self.txt.get("1.0", "end - 1c") #data = self.txt.get("Line.Index", "LastIndex - 1 charector")
data = self.txt.get("1.0", "end - 1l") #data = self.txt.get("Line.Index", "LastIndex - 1 line")

self.txt.insert(1.0, "Hello world,\nhow are you\nI'm Abdul Zoha") #to insert data
self.txt.insert(INSERT, "Hello World, The data to be inserted here...") #insert data from the position of cursor.
self.txt.insert(END, "Hello World, The data to be inserted here...") #insert data to the Last.

self.txt = Text(self.frm, wrap=WORD) #to wrap by word
self.txt = Text(self.frm, wrap=WORD, undo=True) #to undo data pressing by CTRL+Z

"""

class Window:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Widget")
        """calling functions"""
        self.frame()
    def frame(self):
        self.frm = Frame(self.master)
        self.frm.pack(expand=1, fill=BOTH)
        """Label"""
        self.lbl = Label(self.frm, text="My NotePad")
        self.lbl.pack()
        """Text"""
        self.txt = Text(self.frm, wrap=WORD, undo=True)
        self.txt.pack(expand=1, fill=BOTH)
        """Button"""
        self.btn1 = Button(self.frm, text="Print", command=self.getText)
        self.btn2 = Button(self.frm, text="Clear", command=self.clear)
        self.btn3 = Button(self.frm, text="Insert", command=self.insert)
        
        self.btn1.pack(side=LEFT, padx=5, pady=5)
        self.btn2.pack(side=LEFT, padx=5, pady=5)
        self.btn3.pack(side=LEFT, padx=5, pady=5)
    def getText(self):
        data = self.txt.get(1.0, END)
        print(data)
    def clear(self):
        self.txt.delete(1.0, END)
    def insert(self):
        self.txt.insert(END, "Hello World, The data to be inserted here...") #insert data from the position of cursor.


if __name__ == "__main__":
    root = Tk()
    obj = Window(root)
    root.mainloop()