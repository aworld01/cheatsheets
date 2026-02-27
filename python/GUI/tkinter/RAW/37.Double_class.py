from tkinter import*
root = Tk()
root.title("Home")
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def write():
    a = x.get()
    b = y.get()
    c = a+b
    z.set(c)
    x.set("")
    y.set("")

x = DoubleVar()
y = DoubleVar()
z = DoubleVar()

e1 = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", textvariable=x)
e1.place(x=10,y=10, width=150,height=28)

e2 = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", textvariable=y)
e2.place(x=10,y=40, width=150,height=28)

result = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", textvariable=z)
result.place(  x=10,y=70,width=150,height=28)

b1 = Button(root, text="Show",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=write)
b1.place(x=10,y=130,width=150,height=28)

root.mainloop()