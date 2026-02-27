"""
There are 3 ways to insert widgets in Tkinter
1. Place (relwidth,relheight)
relwidth=(Left to Right)
relheight=(Top to Down)

.place(x=10, y=10, width=300, height=200) #(x_margin, y_margin, width, height)
x=(Left to Right)
y=(Top to Bottom)

rel = 0.0 - 1.0
.place(relx=0.02, rely=0.02, relwidth=0.09, relheight=0.09)
relx=x position relative to window size
rely=y position relative to window size

relwidth=width relative to window size
relheight=height relative to window size
"""
from tkinter import*
root = Tk()
root.title("Home")
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")
"""Label"""
lbl = Label(root, text="TOP", bg="red").place(relx=0.02, rely=0.02, relwidth=0.09, relheight=0.09)

root.mainloop()