"""Example-1 (PhotoImage)"""
"""
PhotoImage: It's built-in class in tkinter. It supports only "*.gif" and "*.png" file formats.
example:-
    img = PhotoImage(file="images/voice_recognition.gif") #to display "*.gif" and "*.png" file
"""
# from tkinter import*

# root = Tk()
# root.geometry("500x400")

# img = PhotoImage(file="images/star.png") #make object
# """Label"""
# lbl = Label(root, image=img)
# lbl.pack()

# root.mainloop()



"""Example-2 (Pillow)"""
"""
Image: It's an standard class in pillow, it normaly opens up image and perform the operations.
ImageTk: It's a class that will be using for tkinter, it's specially created to work with tkinter.

ImageTk: it supports atleast all image file formats
example:-
    img = Image.open("images/star.png") #make object
    image = ImageTk.PhotoImage(img) #to make tkinter compatible
"""
from tkinter import*
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x400")

# img = PhotoImage(file="images/star.png") #make object

img = Image.open("images/voice_recognition.gif") #make object
image = ImageTk.PhotoImage(img) #to make tkinter compatible
"""Label"""
lbl = Label(root, image=image)
lbl.pack()

root.mainloop()