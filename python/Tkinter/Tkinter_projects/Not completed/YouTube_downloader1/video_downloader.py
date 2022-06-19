from tkinter import*
from tkinter.ttk import Progressbar
from threading import Thread

"""functions"""
def videoURL():
    url = ent.get()
    print(url)
def downloadVideo():
    pass

root = Tk()
root.title("Video Downloader")
root.geometry("780x500+1120+500")
root.resizable(0,0)
"""change GUI's icon"""
pt = PhotoImage(file = 'icon.png')
root.iconphoto(False, pt)

"""Entrybox"""
ent = Entry(root)

"""Labels"""
title = Label(root, text="Video downloader", font=("chiller", 40, "italic bold"))
total = Label(root, text="Total: ")
total_size = Label(root, text="2000MB")
recieved = Label(root, text="Recieved:" )
recieved_size = Label(root, text="2000")
time_left = Label(root, text="Time Left: ")
time_left_time = Label(root, text="11:11:11")

"""Buttons"""
get = Button(root, text="Get", command=videoURL)
download = Button(root, text="Download")

"""Listbox"""
lbx_frm = Frame(root)
scb = Scrollbar(lbx_frm)
lbx = Listbox(lbx_frm, highlightcolor="blue", highlightthickness=2, yscrollcommand=scb.set)

"""Progressbar"""
prb = Progressbar(root, value=10, length=100)


title.grid(row=0, column=0, columnspan=3)
ent.grid(row=1, column=0, ipadx=200, ipady=2, padx=10, sticky=W)
get.grid(row=1, column=1, ipadx=50, columnspan=2)
lbx_frm.grid(row=2, column=0, rowspan=4, padx=10, pady=20, sticky=W)
scb.pack(side=RIGHT, fill=Y)
scb.config(command=lbx.yview)

lbx.pack(ipadx=200, ipady=70, fill=BOTH)
total.grid(row=2, column=1, sticky=W)
total_size.grid(row=2, column=2, sticky=W)
recieved.grid(row=3, column=1, sticky=W)
recieved_size.grid(row=3, column=2, sticky=W)
time_left.grid(row=4, column=1, sticky=W)
time_left_time.grid(row=4, column=2, sticky=W)
download.grid(row=5, column=1, ipadx=30, columnspan=2)
prb.grid(row=6, column=0, padx=10, ipadx=329, columnspan=4)

root.mainloop()

"""
E = RIGHT
W = LEFT
S = BUTTOM
N = TOP
"""