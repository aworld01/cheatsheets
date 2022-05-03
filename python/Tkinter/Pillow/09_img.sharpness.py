from tkinter import*
from PIL import Image, ImageTk, ImageEnhance

"""
img2 = enhancer.enhance(0)
0: blurry
1: original
2 or more: image with increased sharpness
"""

root = Tk()

img = Image.open("images/a.jpg")
image = ImageTk.PhotoImage(img)
"""Label"""
lbl = Label(root, image=image)
lbl.pack()

enhancer = ImageEnhance.Sharpness(img) #to create object to work with sharpeness
img2 = enhancer.enhance(6)
image2 = ImageTk.PhotoImage(img2)
lbl2 = Label(root, image=image2)
lbl2.pack()

root.mainloop()