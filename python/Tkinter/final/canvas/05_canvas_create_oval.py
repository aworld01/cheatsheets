"""
fill="red" #to fill red color
outline="yellow" #to change outline color
"""

from tkinter import*

root = Tk()
root.geometry("400x400+120+120")

canvas = Canvas(root, width=300, height=300, bg="gray")
canvas.pack(pady=(50,0))
canvas.create_oval(50,50, 200,200, fill="yellow", outline="blue")

root.mainloop()