"""
state=DISABLED
bd=None
"""
from tkinter import*
root = Tk()
root.title("Home")
root.geometry("500x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

btn1 = Button(root, text="Red").pack(pady=10)
btn2 = Button(root, text="Green", state=DISABLED).pack(pady=(0, 10))
btn3 = Button(root, text="Green", bd=None).pack()

root.mainloop()