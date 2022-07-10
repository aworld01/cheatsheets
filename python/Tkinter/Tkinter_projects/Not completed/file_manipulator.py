import os
from tkinter import*
from tkinter import filedialog

from numpy import place

"""functions"""
def select_path():
    if path_ent.get() == "":
        select_folder = filedialog.askdirectory(title="Select folder") #to open popup window to select any folder.
        path_ent.insert(0, select_folder)
def Print():
    data = []
    txt_data = txt.get()
    html_data = html.get()
    css_data = css.get()
    js_data = js.get()
    more_data = more.get().split(",")
    if txt_data == ".txt":
        data.append(".txt")
    if html_data == ".html":
        data.append(".html")
    if css_data == ".css":
        data.append(".css")
    if js_data == ".js":
        data.append(".js")
    if more_data:
        data += more_data
    print(tuple(data))


root = Tk()
root.title("File Manipulator")
root.geometry("600x500+1300+20")
root.resizable(0, 0)

"""Frames"""
frm_fst = Frame(root)
frm_fst.grid(row=0, column=0, sticky=W)

frm_filetype = LabelFrame(root, text="File types", bd=0)
frm_filetype.grid(row=1, column=0, sticky=W, padx=20)

frm_oprations = Frame(root)
frm_oprations.grid(row=3, column=0, padx=20)

frm_lbx = Frame(root)
frm_lbx.grid(row=2, column=0, sticky=W, padx=20, pady=20, ipadx=273, ipady=138)

"""Entry"""
path_ent = Entry(frm_fst)
path_ent.grid(row=0, column=0, padx=20, pady=20, ipadx=135, ipady=4)

"""Buttons"""
path_btn = Button(frm_fst, text="Get Path", command=select_path)
path_btn.grid(row=0, column=1, pady=20)

change_extension = Button(frm_oprations, text="Change Extension", command=Print)
change_extension.grid(row=0, column=0)

rename_file = Button(frm_oprations, text="Rename File", command=Print)
rename_file.grid(row=0, column=1, padx=20)

edit_file = Button(frm_oprations, text="Edit File", command=Print)
edit_file.grid(row=0, column=2)

"""Listbox"""
lbx = Listbox(frm_lbx)
lbx.place(relwidth=1, relheight=1)
"""Scrollbar"""
srb = Scrollbar(frm_lbx)
srb.pack(side=RIGHT, fill=Y)
lbx.config(yscrollcommand=srb.set) #to configure listbox
srb.config(command=lbx.yview) #to configure scrollbar

"""Checkbuttons"""
txt = StringVar()
html = StringVar()
css = StringVar()
js = StringVar()

chk0 = Checkbutton(frm_filetype, text=".txt", offvalue="", onvalue=".txt", variable=txt)
chk0.grid(row=0, column=0)

chk1 = Checkbutton(frm_filetype, text=".html", offvalue="", onvalue=".html", variable=html)
chk1.grid(row=0, column=1)

chk2 = Checkbutton(frm_filetype, text=".css", offvalue="", onvalue=".css", variable=css)
chk2.grid(row=0, column=2)

chk3 = Checkbutton(frm_filetype, text=".js", offvalue="", onvalue=".js", variable=js)
chk3.grid(row=0, column=3)

"""Entry"""
more = Entry(frm_filetype)
more.grid(row=0, column=4, ipadx=83)

root.mainloop()