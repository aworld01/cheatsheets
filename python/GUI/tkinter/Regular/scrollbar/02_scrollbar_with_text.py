from tkinter import*

root = Tk()
root.geometry("600x400")

"""Frame for listbox"""
frm = Frame(root)
frm.place(x=100, y=50)

"""Scrollbar"""
srb = Scrollbar(frm)
srb.pack(side=RIGHT, fill=Y)

"""Text"""
txt = Text(frm, yscrollcommand=srb.set, width=50, height=15)
txt.pack()
srb.config(command=txt.yview) #to link with Text

root.mainloop()