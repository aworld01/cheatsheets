from tkinter import*
from tkinter.ttk import Progressbar
from threading import Thread
from matplotlib.pyplot import text
import pafy
from pydantic import FilePath
from responses import target

"""functions"""
def main():
    t_fetch = Thread(target=fetch_url)
    t_fetch.start()
def fetch_url():
    lbx.delete(0, END)
    url = ent.get()
    data = pafy.new(url)
    streams = data.allstreams #to get all streams
    index = 0
    for i in streams:
        index += 1
        size = i.get_filesize() #to get file size (in Byte)
        MegaByte = size / (1024*1024) #to convert into MB
        MegaByte = f"{MegaByte:.2f} MB"
        quality = i.quality
        extension = i.extension
        mtype = i.mediatype
        item = f"{index}    {MegaByte}   {quality}   {extension}  {mtype}"
        lbx.insert(END, item)
        # video_title.config(text=data.title)
def select(event):
    url = ent.get()
    data = pafy.new(url)
    streams = data.allstreams #to get all streams
    x = lbx.curselection()[0] #to get selected item index
    item = streams[x] #to select by index
    size = item.get_filesize() #to get file size in Bytes
    size = size  / (1024*1024) #to convert into MB
    size = float(f"{size:.2f}")
    total_size.config(text=f"{size} MB")

def get_video():
    get = Thread(target=download)
    get.start()
def download():
    url = ent.get()
    data = pafy.new(url)
    streams = data.allstreams #to get all streams
    x = lbx.curselection()[0] #to get selected item index
    item = streams[x] #to select by index
    item.download(filepath=".", quiet=True, callback=myCallback)
def myCallback(total, recvd, ratio, rate, eta):
    total_size1 = total / (1024*1024)
    total_size1 = float(f"{total_size1:.2f}")

    received1 = recvd / (1024*1024)
    received1 = float(f"{received1:.2f}")

    # ratio = ratio / 1024
    # ratio = float(f"{ratio:.2f}")

    rate = rate / 1024
    rate = float(f"{rate:.2f}")

    estimated_time = f"{eta:.2f} sec"
    
    received.config(text=f"Received: {received1} MB")
    
    time_left.config(text=f"Time left: {estimated_time}")

    # prb.config(length= ttl, value=rcv)
    print(f"Rate: {rate}")
    print(f"Ratio: {ratio}")
    print(f"Estimated time: {estimated_time}")

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
video_title = Label(root, font=("chiller", 16, "italic bold"))
total_size = Label(root, text="Total: ")
received = Label(root, text="Recieved: ")
time_left = Label(root, text="Time Left: ")

"""Buttons"""
get = Button(root, text="Get", command=main)
download_btn = Button(root, text="Download", command=get_video)

"""Listbox"""
lbx_frm = Frame(root)
scb = Scrollbar(lbx_frm)
lbx = Listbox(lbx_frm, highlightcolor="blue", highlightthickness=2, yscrollcommand=scb.set)

"""Progressbar"""
prb = Progressbar(root, value=0, length=100)


title.grid(row=0, column=0, columnspan=2)
ent.grid(row=1, column=0, ipadx=200, ipady=2, padx=10, sticky=W)
get.grid(row=1, column=1, ipadx=50, columnspan=2)
video_title.grid(row=2, column=0, columnspan=3)
lbx_frm.grid(row=3, column=0, rowspan=4, padx=10, pady=20, sticky=W)
scb.pack(side=RIGHT, fill=Y)
scb.config(command=lbx.yview)

lbx.pack(ipadx=200, ipady=60, fill=BOTH)
total_size.grid(row=3, column=1, sticky=W)
received.grid(row=4, column=1, sticky=W)
time_left.grid(row=5, column=1, sticky=W)
download_btn.grid(row=6, column=1, ipadx=30, columnspan=2)
prb.grid(row=7, column=0, padx=10, ipadx=329, columnspan=4)

root.bind("<Double-1>", select)

root.mainloop()

"""
E = RIGHT
W = LEFT
S = BUTTOM
N = TOP
"""