"""
fill="red" #to change line-color
"""
from tkinter import*

root = Tk()
root.geometry("400x400+120+120")

can = Canvas(root, width=200, height=200, bg="gray")
can.pack()
line1 = can.create_line(0,0, 100,100)
line2 = can.create_line(100,100, 0,200, fill="red")

root.mainloop()