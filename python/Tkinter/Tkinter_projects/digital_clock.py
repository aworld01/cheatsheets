from tkinter import*
from time import strftime

def timer():
    string = strftime("%I:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000, timer)

root = Tk()
root.title("Digital Clock")
lbl = Label(root, font=("ds-digital", 80), bg="black", fg="cyan", text="Hello")
lbl.pack(anchor=CENTER)
timer()

root.mainloop()