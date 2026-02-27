"""
photo = PhotoImage(file="avtar.png")
canvas.create_image(0,0, image=photo, anchor=NW)
"""
from tkinter import*

root = Tk()
root.geometry("400x400+120+120")

canvas = Canvas(root, width=400, height=400, bg="gray")
canvas.pack()
photo = PhotoImage(file="avtar.png")
canvas.create_image(0,0, image=photo, anchor=NW)

root.mainloop()