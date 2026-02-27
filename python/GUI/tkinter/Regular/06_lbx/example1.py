from tkinter import*

def populate(event):
    lbx.insert(END, usr_input.get())
    usr_input.delete(0, END)
def show(event):
    x = lbx.get(ACTIVE)
    lbl.config(text=x)
    
    usr_input.delete(0, END)
    usr_input.insert(0, x)
def remove(event):
    x = lbx.delete(0, END)
    usr_input.delete(0, END)

root = Tk()
root.title("Listbox operations")
root.geometry("600x400+900+50")

"""Entry"""
usr_input = Entry(root)
usr_input.grid(row=0, column=0, padx=(50, 0), pady=20)

"""Frame for Listbox"""
frm = Frame(root)
frm.grid(row=1, column=0, ipadx=200, ipady=100, padx=(50, 0))

"""Listbox"""
lbx = Listbox(frm, justify=CENTER)
lbx.place(relwidth=1, relheight=1)

"""Scrollbar"""
srb = Scrollbar(frm)
srb.pack(side=RIGHT, fill=Y)

lbx.config(yscrollcommand=srb.set)
srb.config(command=lbx.yview)

lbl = Label(root, text="test")
lbl.grid(row=2, column=0)

""""Event"""
root.bind("<Return>", populate)
root.bind("<Double-1>", show)
root.bind("<Delete>", remove)


root.mainloop()