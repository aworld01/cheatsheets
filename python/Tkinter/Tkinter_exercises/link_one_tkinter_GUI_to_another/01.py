from tkinter import*
root = Tk()
root.geometry("425x280")

def login():
    e1=Entry()
    e1.pack()

    e2=Entry()
    e2.pack()

    b2 =Button(text="LogIn")
    b2.pack()

b1 = Button(text="Click!!", command=login)
b1.pack()

root.mainloop()