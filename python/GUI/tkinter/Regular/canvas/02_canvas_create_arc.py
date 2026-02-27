"""
extent=120 #to change degree
"""
from tkinter import*

root = Tk()
root.geometry("400x400+120+120")

can = Canvas(root, width=400, height=400, bg="gray")
can.pack()
# chart1 = can.create_arc(100,100, 200,200)
chart2 = can.create_arc(100,100, 200,200, extent=120)

root.mainloop()