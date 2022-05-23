from tkinter import*
root = Tk()
root.geometry("425x350")

def login():
    f2=Frame()
    f2.place(x=0,y=0,width=425,height=350)

    u=Label(f2,text="LogIn Page")
    u.place(x=150,y=10)

    u1=Label(f2,text="Enter name: ")
    u1.place(x=100,y=80)

    e1=Entry(f2,font=("",12))
    e1.place(x=200,y=80,width=120)

    u1=Label(f2,text="Enter passwd: ")
    u1.place(x=100,y=130)
    e1=Entry(f2,font=("",12),show="*")
    e1.place(x=200,y=130,width=120)

    b2 =Button(f2,text="LogIn",command=login)
    b2.place(x=150,y=200,width=80,height=40)

    b2 =Button(f2,text="<-",command=home)
    b2.place(x=2,y=3)
    

def regis():
    f3=Frame()
    f3.place(x=0,y=0,width=425,height=350)

    e1=Entry(f3)
    e1.pack()

    e2=Entry(f3)
    e2.pack()

    e3=Entry(f3)
    e3.pack()

    b2 =Button(f3,text="Back",command=home)
    b2.pack()


def home():
    f1=Frame()
    f1.place(x=0,y=0,width=425,height=350)

    b1 = Button(f1,text="LogIn", command=login)
    b1.place(x=100,y=50,width=80,height=40)

    b2 = Button(f1,text="Regis", command=regis)
    b2.place(x=200,y=50,width=80,height=40)
home()


root.mainloop()