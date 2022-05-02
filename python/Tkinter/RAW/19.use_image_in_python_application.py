from tkinter import*
from PIL import ImageTk

root = Tk()
root.title("Tkinter")
root.geometry("800x500+250+20")
root.resizable(False,False)
root.config(bg="#262626")

"""
## PhotoImage
image=icon
image=icon,compound=LEFT/RIGHT

pip install pillow
from PIL ImageTk
"""
## PhotoImage
# icon = PhotoImage(file="images/01.png")
# lbl_img = Label(root,text="Username",image=icon,compound=RIGHT).place(x=50,y=50)


## ImageTk.PhotoImage
icon = ImageTk.PhotoImage(file="images/bg.jpg")
lbl_img = Label(root,image=icon).place(x=0,y=0)

root.mainloop()