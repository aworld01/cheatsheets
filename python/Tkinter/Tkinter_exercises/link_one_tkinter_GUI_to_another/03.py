from tkinter import*
root = Tk()
root.geometry("425x280")

def login():
    f2=Frame()
    f2.place(x=0,y=0,width=425,height=280)
    e1=Entry(f2)
    e1.pack()
    e2=Entry(f2)
    e2.pack()
    b2 =Button(f2,text="back",command=home)
    b2.pack()
def home():
    f1=Frame()
    f1.place(x=0,y=0,width=425,height=280)
    b1 = Button(f1,text="Click!!", command=login)
    b1.pack()
home()
root.mainloop()