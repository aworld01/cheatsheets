"""
3. Grid System
Row, Column, pady, padx, ipadx, ipady, columnspan=2, rowspan=2,  sticky=W (sticky=W, E, N, S)

grid(row=0,column=1, sticky=W)
columnspan=2

-------GRID SYSTEM--------
lbl = Label(root,text="GRID SYSTEM").grid(row=0,column=0)
lbl = Label(root,text="GRID SYSTEM").grid(row=1,column=0)
lbl = Label(root,text="GRID SYSTEM").grid(row=2,column=0)
"""
from tkinter import*

root=Tk()
root.geometry("500x500")
Font = ("Times new roman", 20, "bold")

"""Frame"""
frm = Frame(root)
frm.pack()

title = Label(frm, text="This is a grid layout Example", font=Font).grid(row=0, column=0, pady=(100, 30), columnspan=2)
lbl1 = Label(frm, text="Entry One")
ent1 = Entry(frm)
lbl1.grid(row=1, column=0, pady=(10,0), padx=(10,0))
ent1.grid(row=1, column=1, pady=(10,0), padx=(10,0))

lbl2 = Label(frm, text="Entry One")
ent2 = Entry(frm)
lbl2.grid(row=2, column=0, pady=(10,0), padx=(10,0))
ent2.grid(row=2, column=1, pady=(10,0), padx=(10,0))

root.mainloop()