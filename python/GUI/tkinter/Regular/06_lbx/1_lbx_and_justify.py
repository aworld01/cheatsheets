from tkinter import*
"""
lbx = Listbox(frm,justify=LEFT) to align list items in LEFT (default).
lbx = Listbox(frm,justify=CENTER): to align list items in CENTER.
lbx = Listbox(frm,justify=RIGHT) to align list items in RIGHT.
"""
root = Tk()
root.title("Home")
root.geometry("700x400+1820+0") #root.geometry("widthxheight+x_pos+y_pos)
root.resizable(0,0)
root.config(bg="gray") #to change background-color
"""frame"""
frm = Frame(root, bg="#1d1d1d")
frm.place(x=20, y=20, relwidth=.60, relheight=.9)
"""List box"""
lbx = Listbox(frm,justify=CENTER)
lbx.place(relheight=1, relwidth=1)
"""add data into list"""
lbx.insert(END, "Hello")
lbx.insert(END, "World")
"""Scrollbar"""
scrollbar = Scrollbar(frm)
scrollbar.pack(side=RIGHT, fill=Y)
lbx.config(yscrollcommand=scrollbar.set) #to configure listbox
scrollbar.config(command=lbx.yview) #to configure scrollbar

root.mainloop()