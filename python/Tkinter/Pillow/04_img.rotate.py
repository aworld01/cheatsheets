from tkinter import*
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x400")

img = Image.open("images/a.jpg")
img = img.rotate(45) #to rotate
image = ImageTk.PhotoImage(img)
"""Label"""
lbl = Label(root, image=image)
lbl.pack()

root.mainloop()