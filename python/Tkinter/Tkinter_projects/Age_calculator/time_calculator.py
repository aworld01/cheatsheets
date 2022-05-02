from tkinter import*
from datetime import datetime
from tkinter import font
from PIL import ImageTk, Image
from matplotlib import image

# """define a function"""
def calculate(event):
    n = name.get()
    bmonth = int(mon.get())
    byear = int(yea.get())

    now = datetime.now()
    month = int(now.strftime("%m"))
    year = int(now.strftime("%Y"))
    if byear<year:
        if bmonth<month:
            x = year - byear
            y = month - bmonth
            msg.config(text=f"Hello {n} you are: {x} years and {y} months old...")
        else:
            x = (year - byear) - 1
            y = 12 - (bmonth - month)
            msg.config(text=f"Hello {n} you are: {x} years and {y} months old...")
    else:
        msg.config(text=f"Check your birth year once again...")
#                 nm.set(), da.set(""), mo.set(""), ye.set("")

root = Tk()
root.title("Time calculator")
root.geometry("600x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

"""assign labels"""
name_lbl = Label(root, text="Name: ").place(x=20, y=20)
day_lbl = Label(root, text="Day: ").place(x=20, y=60)
month_lbl = Label(root, text="Month: ").place(x=20, y=100)
year_lbl = Label(root, text="Year: ").place(x=20, y=140)
"""insert image"""
img = Image.open("img.jpg")
img = img.resize((280, 370))
img = ImageTk.PhotoImage(img)
img_lbl = Label(root, image=img).place(x=310, y=10, width=280, height=370)

msg = Label(root, bg="gray", font="bold")
msg.pack(side=BOTTOM, pady=10)

"""assign entries"""
nm = StringVar()
da = StringVar()
mo = StringVar()
ye = StringVar()
name = Entry(root, textvariable=nm)
name.place(x=80, y=20)
day = Entry(root, textvariable=da)
day.place(x=80, y=60)
mon = Entry(root, textvariable=mo)
mon.place(x=80, y=100)
yea = Entry(root, textvariable=ye)
yea.place(x=80, y=140)

"""assign a button"""
btn = Button(root, text="CALCULATE", command=lambda: calculate("event"))
btn.place(x=110, y=190)
root.bind('<Return>', calculate)

root.mainloop()