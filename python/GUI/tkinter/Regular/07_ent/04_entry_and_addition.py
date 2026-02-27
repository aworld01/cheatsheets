from tkinter import*
"""define a function"""
def show():
    nm1 = num1.get()
    nm2 = num2.get()
    total = int(nm1)+int(nm2)
    msg.config(text=total)
    n1.set(""), n2.set("")

root = Tk()
root.title("Home")
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

"""assign labels"""
num1_lbl = Label(root, text="Number1: ")
num1_lbl.place(x=20, y=20)
num2_lbl = Label(root, text="Number2: ")
num2_lbl.place(x=20, y=60)
msg = Label(root, text="________")
msg.pack()

"""assign entries"""
n1 = StringVar() #string variable to perform set method
n2 = StringVar() #string variable to perform set method
num1 = Entry(root, textvariable=n1)
num1.place(x=100, y=20)
num2 = Entry(root, textvariable=n2)
num2.place(x=100, y=60)

"""assign a button"""
btn = Button(root, text="SHOW", command=show)
btn.place(x=20, y=100)

root.mainloop()