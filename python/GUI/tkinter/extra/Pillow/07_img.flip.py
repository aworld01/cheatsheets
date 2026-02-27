from tkinter import*
from PIL import Image, ImageTk

root = Tk()

img = Image.open("images/a.jpg")
image = ImageTk.PhotoImage(img)
"""Label"""
lbl = Label(root, image=image)
lbl.pack()

# img2 = img.transpose(Image.FLIP_LEFT_RIGHT) #to flip image left to right
img2 = img.transpose(Image.FLIP_TOP_BOTTOM) #to flip image left to right
image2 = ImageTk.PhotoImage(img2)
lbl2 = Label(root, image=image2)
lbl2.pack()

root.mainloop()