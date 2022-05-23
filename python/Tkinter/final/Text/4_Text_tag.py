"""
CREATE TAG
self.txt.tag_add("red", "1.0", "1.0 lineend") #name of the tag, position of the tag

CONFIGURE TAG
self.txt.tag_config("red", background="red", font=("Verdana", 12)) #to configure tag

DELETE TAG
self.txt.tag_delete("red") #to delete tag

REMOVE TAG
self.txt.tag_remove("red", "1.0 wordstart", "1.0 wordend")
"""
from tkinter import*

class Window:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Widget")

        """Scrollbar"""
        self.srb = Scrollbar(self.master)
        self.srb.pack(side=RIGHT, fill=Y)
        """Text"""
        self.txt = Text(self.master, yscrollcommand=self.srb.set)
        self.txt.pack(expand=1, fill=BOTH)
        """Scrollbar configuration"""
        self.srb.config(command=self.txt.yview)
        """inserting data"""
        self.txt.insert(1.0, "Hello world,\nhow are you\nI'm Abdul Zoha")

        """creating tag"""
        self.txt.tag_add("red", "1.0", "1.0 lineend") #name of the tag, position of the tag
        self.txt.tag_add("yellow", "2.0", "2.0 lineend")
        """applying tag"""
        self.txt.tag_config("red", background="red", font=("Verdana", 12))
        self.txt.tag_config("yellow", background="yellow", font=("Times", 20))
        

if __name__ == "__main__":
    root = Tk()
    obj = Window(root)
    root.mainloop()