from tkinter import*
from PIL import Image, ImageTk

root = Tk()

img = Image.open("images/a.jpg")
# img = img.rotate(45) #to rotate
img = img.rotate(45, expand=True) #to rotate without lose any part of image
image = ImageTk.PhotoImage(img)
"""Label"""
lbl = Label(root, image=image)
lbl.pack()

root.mainloop()