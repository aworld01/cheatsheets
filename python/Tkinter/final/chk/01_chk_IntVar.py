from tkinter import*

root = Tk()
root.geometry("400x400")

"""function"""
def checkb():
    lbl.config(text=check.get())

"""Checkbutton"""
check = IntVar()
chk = Checkbutton(root, text="Accept our Terms and Condition", offvalue=0, onvalue=1, variable=check, command=checkb)
chk.pack()

"""Label"""
lbl = Label(root)
lbl.pack()

root.mainloop()