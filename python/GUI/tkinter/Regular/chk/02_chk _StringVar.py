from tkinter import*

root = Tk()
root.geometry("400x400")

"""function"""
def checkb():
    lbl.config(text=check.get())

"""Checkbutton"""
check = StringVar()
chk = Checkbutton(root, text="Accept our Terms and Condition", offvalue="Off", onvalue="On", variable=check, command=checkb)
chk.deselect() #to set deselect mode
# chk.select() #to set select mode
chk.pack()

"""Label"""
lbl = Label(root)
lbl.pack()

root.mainloop()