"""
2. Pack
.pack(padx=10, pady=10) #to give outside padding = margin
padx=left, right
pady=top, bottom
pady=(10,0) #top
pady=(0,10) #bottom

.pack(ipadx=10, ipady=10) #to give inside padding = padding


.pack(side=TOP) (default)
.pack(side=BOTTOM) #to align item at bottom
.pack(side=LEFT) #to align item at left
.pack(side=RIGHT) #to align item at right

.pack(expand=0) (default)
.pack(expand=1) #to work at Y axis
.pack(expand=True) #to work at Y axis

.pack(fill=NONE) (default)
.pack(fill=X) #to fill LEFT and RIGHT
.pack(fill=Y, expand=1) #to fill TOP and BOTTOM
.pack(fill=BOTH, expand=1) #to fill BOTH side

.pack(fill=1, anchor=N) North=TOP (default)
.pack(fill=1, anchor=S) South=BOTTOM
.pack(fill=1, anchor=E) East=RIGHT
.pack(fill=1, anchor=W) West=LEFT

.pack(side=RIGHT, anchor=NE) North, East (TOP RIGHT)
.pack(side=LEFT, anchor=NW) North, West (TOP LEFT)
.pack(side=RIGHT, anchor=SE) South, East (BOTTOM RIGHT)
.pack(side=LEFT, anchor=SW) South, West (BOTTOM LEFT)
"""
from tkinter import*
root = Tk()
root.title("Home")
root.geometry("700x400+1820+0")
# root.resizable(0,0)
root.config(bg="gray")
"""Label"""
lbl1 = Label(root, text="TOP", bg="red").pack(side=TOP, pady=(40, 0))
lbl2 = Label(root, text="TOP", bg="red").pack(side=LEFT, expand=True)
lbl3 = Label(root, text="TOP", bg="red").pack(side=LEFT, expand=True)

root.mainloop()