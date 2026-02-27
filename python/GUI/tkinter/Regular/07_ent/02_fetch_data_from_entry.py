from tkinter import*
"""


show="*": to hide text with '*' symbol
"""
def show():
    data = ent.get()
    lbl.config(text=data, bg="green")
    en.set("") #to clear entry box

root = Tk()
root.title("Home")
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")
"""assign a entry"""
en = StringVar() #to work with set method
ent = Entry(root, textvariable=en)
ent.place(x=20, y=20)

"""assign a button"""
btn = Button(root, text="SHOW", command=show).place(x=20, y=60)
"""assing a label"""
lbl = Label(root,text="demo text")
lbl.pack()

root.mainloop()