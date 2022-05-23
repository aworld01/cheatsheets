from tkinter import*

"""function"""
def show():
    name = usr_name.get()
    mail = email.get()
    value = check.get()
    gen = gender.get()
    data = f"You are: {gen}\nYour name is: {name}\nYour email is: {mail}"
    if value == 1:
        result.config(text=data)
        usr_name.delete(0, END)
        email.delete(0, END)
        gender.set("")
        check.set(0)
    else:
        result.config(text="Please accept Terms and Conditions")

root = Tk()
root.title("User Entry Form")
root.geometry("500x500")
"""Label"""
Label(root, text="USER ENTRY FORM", bg="#262626", fg="white", font=("arial",30,"bold")).place(x=0, y=0, relwidth=1)
Label(root, text="USER NAME", font=("times new roman", 20)).place(x=20, y=80)
Label(root, text="EMAIL", font=("times new roman", 20)).place(x=20, y=130)
gender = Label(root, text="Gender",font=("times new roman", 20)).place(x=20, y=180)
"""Entry"""
usr_name = Entry(root)
usr_name.place(x=190, y=82, height=30)
email = Entry(root)
email.place(x=190, y=132, height=30)
"""Radiobutton"""
gender = StringVar()
gender.set("male")
male = Radiobutton(root,text="Male",value="male", font=("times new roman", 20),variable=gender)
male.place(x=100, y=180)
female = Radiobutton(root,text="Female",value="female", font=("times new roman", 20),variable=gender)
female.place(x=200, y=180)
"""Checkbutton"""
check = IntVar()
ckb = Checkbutton(root, text="Accept our Terms and Condition", font=("times new roman", 20), onvalue=1, offvalue=0, variable=check)
ckb.place(x=20, y=230)
"""Label"""
result = Label(root, text="testing....", font=("times new roman", 18))
result.place(x=20, y=350)
"""Button"""
Button(root, text="SHOW", font=("times new roman", 20), command=show).place(x=200, y=300)

root.mainloop()