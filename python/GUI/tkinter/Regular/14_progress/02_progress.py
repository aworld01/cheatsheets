from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Progressbar

n = 0
def clicked():
    global n
    if n<5:
        n+=1 #to increase progressbar
        var.set(n) #to increase progressbar
        lbl.config(text="Pressed: "+str(n)+" out of five times.")
    else:
        messagebox.showwarning("Warning", "You already pressed 5 times")

root = Tk()
root.geometry("500x500")
"""define Progressbar"""
var = IntVar()
var.set(0) #to increase progressbar
pb = Progressbar(root, orient=HORIZONTAL, mode="determinate", maximum=5, length=100, variable=var)
pb.pack(pady=20)
"""define Button"""
btn = Button(root, text="Click me five times", command=clicked)
btn.pack(pady=20)
"""define Label"""
lbl = Label(root, text="test", font=("Consolas", 20, "bold"))
lbl.pack()

root.mainloop()