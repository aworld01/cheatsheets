from tkinter import*
from datetime import datetime

root = Tk()
root.title("")
root.config(bg="#3d3d3d")
"""function"""
def clock():
    time = datetime.now()
    day = time.strftime("%A")
    hour = time.strftime("%I:%M:%S")
    date = time.strftime("%d/%m/%Y")
    lbl_day.config(text=day)
    lbl_hour.config(text=hour)
    lbl_date.config(text=date)
    """after function"""
    lbl_hour.after(1000, clock)

"""fram for date and time"""
lbl_frm = Frame(root, bg="#3d3d3d")
lbl_frm.pack()

"""labels for date and time"""
lbl_hour = Label(lbl_frm, font=("ds-digital", 80), bg="#3d3d3d", fg="#21c25c")
lbl_hour.grid(row=0, column=0)

lbl_day = Label(lbl_frm, font=("ds-digital", 30), bg="#3d3d3d", fg="#21c25c")
lbl_day.grid(row=1, column=0, sticky=W)

lbl_date = Label(lbl_frm, font=("ds-digital", 30), bg="#3d3d3d", fg="#21c25c")
lbl_date.grid(row=2, column=0, sticky=W)

clock()

root.mainloop()