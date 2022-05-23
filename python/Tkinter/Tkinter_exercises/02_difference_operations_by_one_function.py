from tkinter import*

root = Tk()
root.title("Home")
root.geometry("400x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def show(op):
    a = int(x.get())
    b = int(y.get())
    if (op==1):
        c = a+b
        lbl.config(text=c, bg="gray")
    if (op==2):
        c = a-b
        lbl.config(text=c, bg="gray")
    if (op==3):
        c = a*b
        lbl.config(text=c, bg="gray")

x = StringVar()
y = StringVar()

"""Entry"""
ent1 = Entry(root, bg="yellow", fg="red", textvariable=x)
ent1.pack(pady=10)
ent2 = Entry(root, bg="yellow", fg="red", textvariable=y)
ent2.pack(pady=10)
"""Label"""
lbl = Label(root, bg="#262626")
lbl.pack(pady=50)

"""Frame"""
frm = Frame(root, bg="#262626")
frm.place(x=160, y=90, width=90, height=30)

"""Buttons"""
btn1 = Button(frm, text="+",bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=lambda:show(1))
btn1.place(x=0,y=0,width=28,height=28)

btn2 = Button(frm, text="-",bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=lambda:show(2))
btn2.place(x=30,y=0,width=28,height=28)

btn3 = Button(frm, text="x",bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=lambda:show(3))
btn3.place(x=60,y=0,width=28,height=28)

root.mainloop()