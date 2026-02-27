from tkinter import*
import os
from PIL import ImageTk, Image

path = "/home/neo/Pictures"
images = os.listdir(path)
n = 0

"""functions"""
def forward():
    global n
    global img1
    global lbl

    n += 1
    img1 = os.path.join(path, images[n])
    lbl.grid_forget() #to remove lbl content
    
    img2 = Image.open(img1)
    img2 = img2.resize((600, 400))
    img3 = ImageTk.PhotoImage(img2)
    """insert a Label"""
    lbl = Label(root, image=img3)
    lbl.grid(row=0, column=0, columnspan=3)
    print(img1)
def back():
    global n
    global img1
    global lbl

    if n>0:
        n -= 1
    img1 = os.path.join(path, images[n])
    lbl.grid_forget() #to remove lbl content
    
    img2 = Image.open(img1)
    img2 = img2.resize((600, 400))
    img3 = ImageTk.PhotoImage(img2)
    """insert a Label"""
    lbl = Label(root, image=img3)
    lbl.grid(row=0, column=0, columnspan=3)
    print(img1)

root = Tk()
root.title("")
"""make image object"""
img1 = Image.open("/home/neo/Pictures/1202~1.jpg")
img1 = img1.resize((600, 400))
img = ImageTk.PhotoImage(img1)
"""insert a Label"""
lbl = Label(root, image=img)
lbl.grid(row=0, column=0, columnspan=3)
"""assign buttons"""
btn1 = Button(root, text="<<", command=back)
btn2 = Button(root, text="Exit", command=root.quit)
btn3 = Button(root, text=">>", command=forward)
"""place buttons"""
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)


root.mainloop()