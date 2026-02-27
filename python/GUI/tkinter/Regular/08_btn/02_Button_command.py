'''
command="show": to show text.
'''
from tkinter import*
"""define a function"""
def show():
    lbl.config(text="Hello world", bg="white")

root = Tk()
root.title("Home")
root.geometry("500x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")
"""defining a Label"""
lbl = Label(root, bg="#262626")
lbl.pack(pady=20)
"""defining a Button"""
btn = Button(root, text="show", command=show)
btn.pack()

root.mainloop()