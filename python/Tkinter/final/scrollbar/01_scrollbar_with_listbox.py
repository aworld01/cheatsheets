from tkinter import*

root = Tk()
root.geometry("600x400")

"""Frame for listbox"""
frm = Frame(root)
frm.place(x=100, y=50)

"""Scrollbar"""
srb = Scrollbar(frm)
srb.pack(side=RIGHT, fill=Y)

"""Listbox"""
lbx = Listbox(frm, yscrollcommand=srb.set)
lbx.pack()
srb.config(command=lbx.yview) #to link with listbox

"""inserting data into listbox"""
for item in range(50):
    lbx.insert(END, item)


root.mainloop()