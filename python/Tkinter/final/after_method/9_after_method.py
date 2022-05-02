from tkinter import*

chat = {
    "Hello": "Hi", 
    "How are you": "I'm fine sir",
    "": ""
    }

class After:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("After method")

        """Entry"""
        self.ent = Entry(self.root)
        self.ent.pack(pady=20)

        """Label"""
        self.lbl = Label(self.root)
        self.lbl.pack()

        self.populate()

    def populate(self):
        x = self.ent.get().capitalize()
        for ask, ans in chat.items():
            if x in ask:
                self.lbl.config(text=ans)
            elif x == "":
                self.lbl.config(text="")

        self.root.after(100, self.populate)

if __name__ == "__main__":
    root = Tk()
    obj = After(root)
    root.mainloop()