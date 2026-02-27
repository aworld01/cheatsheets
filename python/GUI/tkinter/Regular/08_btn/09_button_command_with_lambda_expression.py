"""
command=lambda:show("key") #with lambda expression
"""

from tkinter import*
"""define a function"""
def show(key):
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
btn = Button(root, text="show", command=lambda:show("key"))
btn.pack()

root.mainloop()