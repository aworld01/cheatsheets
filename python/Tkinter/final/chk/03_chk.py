from tkinter import*

"""function"""
def show():
    data = check.get()
    if data == 1:
        lbl.config(text="You checked")
        # check.set(0) #to set uncheck
    else:
        lbl.config(text="Please check first....")

root = Tk()
root.title("Checkbutton")
root.geometry("500x500")
"""Checkbutton"""
check = IntVar()
chk = Checkbutton(root, text="Accept our Terms and Condition", font=("times new roman", 20), onvalue=1, offvalue=0, variable=check)
chk.pack()
"""Button"""
Button(root, text="SHOW", command=show).pack(pady=20)
"""Label"""
lbl = Label(root)
lbl.pack()

root.mainloop()