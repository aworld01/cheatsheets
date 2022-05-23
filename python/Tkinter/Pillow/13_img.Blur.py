from tkinter import*
from PIL import Image, ImageTk, ImageFilter

"""
ImageFilter.GaussianBlur(radius=2) Default
You can increase radius
"""

root = Tk()

img = Image.open("images/a.jpg")
image = ImageTk.PhotoImage(img)
"""Label"""
lbl = Label(root, image=image)
lbl.pack()

# enhancer = ImageFilter.GaussianBlur() #to create object to work with Blur
enhancer = ImageFilter.GaussianBlur(4)
img2 = img.filter(enhancer)
image2 = ImageTk.PhotoImage(img2)
lbl2 = Label(root, image=image2)
lbl2.pack()

root.mainloop()