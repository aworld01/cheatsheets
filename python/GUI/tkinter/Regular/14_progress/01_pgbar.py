"""
DEFAULTS
orient=VERTICAL / HORIZONTAL (default)
mode = "indeterminate" / "determinate" (default)
value= 5 / 0 (default)

determinate #to fix oprations
inderminate #to show running task

"determinate"
length #size of Progressbar
value #increasing value
miximum #stop value
orient #direction of Progressbar
pgbar[value]=30 #to increase value

"indeterminate"
length=400
orient=HORIZONTAL
mode="indeterminate"
pgbar.start(10)
pgbar.stop()
"""
from tkinter import*
from tkinter.ttk import Progressbar

root = Tk()
root.title("Progressbar")
root.geometry("500x500")

"""Progressbar(determinate)"""
"""function"""
# n = 0
# def increase():
#     global n
#     n += 5
#     pgbar.config(value=n)

# pgbar = Progressbar(root, length=400, maximum=100)
# pgbar.pack(pady=20)
# """Button"""
# Button(root, text="SHOW", command=increase).pack()

"""Progressbar(indeterminate)"""
"""function"""
def run():
    pgbar.start(10)
def pause():
    pgbar.stop()

pgbar = Progressbar(root, length=400, mode="indeterminate")
pgbar.pack(pady=20)
"""Button"""
Button(root, text="START", command=run).pack()
Button(root, text="STOP", command=pause).pack()

root.mainloop()