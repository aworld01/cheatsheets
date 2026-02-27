from tkinter import*
from PIL import Image, ImageTk
"""function"""
def welcome():
    usr.destroy()
    pwd.destroy()
    btn.destroy()
    """add a welcome message"""
    canvas.create_text(160, 450, text="Welcome!", font=("Helvetica", 40), fill="white")
w = 323
h = 576

root = Tk()
root.title("")
root.geometry(f"{w}x{h}")
root.resizable(0, 0)
"""define background-image"""
img = ImageTk.PhotoImage(file="img.jpeg")
"""define Canvas"""
canvas = Canvas(root, width=w, height=h, bd=0, highlightthickness=0)
canvas.pack(fill=BOTH, expand=1)
"""put the image on the canvas"""
canvas.create_image(0,0, image=img, anchor=NW)
"""define Entry Boxes"""
usr = Entry(root, font=("Helvetica", 16), width=14, fg="#336d92", bd=0)
pwd = Entry(root, font=("Helvetica", 16), width=14, fg="#336d92", show="*")
"""add the Entry boxes to the canvas"""
usr_win = canvas.create_window(20, 150, anchor=NW, window=usr)
pwd_win = canvas.create_window(20, 200, anchor=NW, window=pwd)
"""define a Button"""
btn = Button(root, text="Click", font=("Helvetica", 16), width=12, fg="#336d92", command=welcome)
"""add the Button to the canvas"""
usr_btn = canvas.create_window(20, 250, anchor=NW, window=btn)




root.mainloop()