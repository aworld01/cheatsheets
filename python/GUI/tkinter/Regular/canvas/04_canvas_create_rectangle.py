"""
fill="red" #to fill red color
outline="yellow" #to change outline color
"""

from tkinter import*

root = Tk()
root.geometry("400x400+120+120")

canvas = Canvas(root, width=400, height=400, bg="gray")
canvas.pack()
canvas.create_rectangle(100,100, 300,250, fill="red", outline="yellow")

root.mainloop()