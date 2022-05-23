from tkinter import*
"""
en1 = StringVar() #string value to perform set method
en2 = IntVar() #int value to perform set method
en1.set(""), en2.set("") #to clear ent1 and ent2
"""
"""define a function"""
def show():
    nm = name.get()
    a = age.get()
    msg.config(text=f"Hello {nm} your age is {a}")
    nam.set(""), ag.set("")

root = Tk()
root.title("Home")
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

"""assign labels"""
name_lbl = Label(root, text="Name: ")
name_lbl.place(x=20, y=20)
age_lbl = Label(root, text="Age: ")
age_lbl.place(x=20, y=60)
msg = Label(root, text="________")
msg.pack()

"""assign entries"""
nam = StringVar() #string variable to perform set method
ag = StringVar() #string variable to perform set method
name = Entry(root, textvariable=nam)
name.place(x=80, y=20)
age = Entry(root, show="*", textvariable=ag)
age.place(x=80, y=60)

"""assign a button"""
btn = Button(root, text="SHOW", command=show)
btn.place(x=20, y=100)

root.mainloop()