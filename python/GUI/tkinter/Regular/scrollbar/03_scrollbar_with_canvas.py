from tkinter import*

root = Tk()
root.geometry("600x400")

"""Frame for listbox"""
frm = Frame(root)
frm.place(x=100, y=50)

"""Scrollbar"""
srb = Scrollbar(frm)
srb.pack(side=RIGHT, fill=Y)

"""Canvas"""
can = Canvas(frm, width=300, height=300, bg="white", scrollregion=(0, 0, 500, 500), yscrollcommand=srb.set)
can.pack()
srb.config(command=can.yview) #to link with Text

root.mainloop()