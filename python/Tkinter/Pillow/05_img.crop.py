from tkinter import*
from PIL import Image, ImageTk

root = Tk()

img = Image.open("images/a.jpg")
image = ImageTk.PhotoImage(img)
"""Label"""
lbl = Label(root, image=image)
lbl.pack()

area = (200, 50, 600, 300) #(x, y, width, height)
img2 = img.crop(area) #to crop image
image2 = ImageTk.PhotoImage(img2)
lbl2 = Label(root, image=image2)
lbl2.pack()

root.mainloop()