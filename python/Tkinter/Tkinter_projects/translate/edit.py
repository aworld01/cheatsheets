from tkinter import*
from tkinter import messagebox
import dbhelper

"""functions"""
def update():
    inp1 = input1.get()
    inp2 = input2.get()
    if(len(inp1) == 0):
        messagebox.showerror('ERROR', 'No data available\nPlease enter some task')
    dbhelper.updatedata(inp1, inp2)
    input1.delete(0, END)
    input2.delete(0, END)
    populate()
    populate2()
def add(event):
    inp1 = input1.get()
    inp2 = input2.get()
    if(len(inp1) == 0):
        messagebox.showerror('ERROR', 'No data available\nPlease enter some task')
    else:
        dbhelper.insertdata(inp1, inp2)
        input1.delete(0, END)
        input2.delete(0, END)
        populate()
        populate2()
        records()
def delete():
    inp1 = input1.get()
    inp2 = input2.get()
    if(len(inp1) == 0):
        messagebox.showerror('ERROR', 'No data available\nPlease enter some task')
    else:
        dbhelper.deletebyid(inp1)
        input1.delete(0, END)
        input2.delete(0, END)
        populate()
        populate2()
        records()
def populate():
    lbx.delete(0, END)
    for rows in dbhelper.show():
        lbx.insert(END, rows[1])
def populate2():
    lbx2.delete(0, END)
    for rows in dbhelper.show():
        lbx2.insert(END, rows[2])
def records():
    cnt = f"Total: {dbhelper.count1()}"
    total.config(text=cnt)

root = Tk()
root.title("Translator")
root.geometry("1620x500+1820+0")
root.config(bg="maroon")
root.resizable(0,0)
pt = PhotoImage(file = 'icon.png')
root.iconphoto(False, pt)

main = Frame(root, bg="maroon")
main.pack()

Label(main, text="ARTIFICIALWORLD01", font=("Arial",30, "bold")).grid(row=0, column=0, pady=(20, 10), columnspan=2)

total = Label(main, text="Total:", padx=10)
total.grid(row=1, column=0, columnspan=2)
records()

Label(main, text="TRANSLATE", padx=10, bg="maroon", fg="white").grid(row=2, column=0)

input1 = Entry(main, font=("arial", 16, "bold"))
input1.grid(row=3, column=0, ipadx=260)

Label(main, text="TRANSLATED", padx=10, bg="maroon", fg="white").grid(row=2, column=1)

input2 = Entry(main, font=("arial", 16, "bold"))
input2.grid(row=3, column=1, ipadx=260)

Label(main, text="LIST-1", padx=10, bg="maroon", fg="white").grid(row=5, column=0, pady=(10, 0))

Label(main, text="LIST-2", padx=10, bg="maroon", fg="white").grid(row=5, column=1, pady=(10, 0))

"""defining a Frame for listbox-1"""
frm_lbx1 = Frame(main,bd=2,relief=RIDGE)
frm_lbx1.grid(row=6, column=0, ipadx=390, ipady=100, padx=(0,10))

"""defining a Listbox"""
lbx = Listbox(frm_lbx1,justify=CENTER,font=("arial", 18, "bold"))
lbx.place(x=0, y=0, relwidth=1, relheight=1)

"""defining a Scrollbar"""
scroll = Scrollbar(frm_lbx1,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)

"""to configure scrollbar with listbox"""
lbx.config(yscrollcommand=scroll.set)
scroll.config(command=lbx.yview)
populate()

"""defining a Frame for listbox-2"""
frm_lbx2 = Frame(main,bd=2,relief=RIDGE)
frm_lbx2.grid(row=6, column=1, ipadx=390, ipady=100)

"""defining a Listbox"""
lbx2 = Listbox(frm_lbx2,justify=CENTER,font=("arial", 18, "bold"))
lbx2.place(x=0, y=0, relwidth=1, relheight=1)

"""defining a Scrollbar"""
scroll2 = Scrollbar(frm_lbx2,orient=VERTICAL)
scroll2.pack(side=RIGHT,fill=Y)

"""to configure scrollbar with listbox"""
lbx2.config(yscrollcommand=scroll2.set)
scroll2.config(command=lbx2.yview)
populate2()

updated = Label(main, text="Last update: 24/03/2022", bg="maroon", fg="white")
updated.grid(row=7, column=0, columnspan=2, pady=(10,0))

frm_btn = Frame(root, bg="maroon")
frm_btn.pack()
upload = Button(frm_btn, text="ADD", command=lambda:add("event"))
upload.grid(row=0, column=0, pady=(10, 0), padx=(0, 50))
upd = Button(frm_btn, text="UPDATE", command=update).grid(row=0, column=1, pady=(10, 0), padx=(0, 50))
delete = Button(frm_btn, text="DELETE", command=delete).grid(row=0, column=2, pady=(10, 0), padx=(0, 50))
close = Button(frm_btn, text="CLOSE", command=root.destroy).grid(row=0, column=3, pady=(10, 0))

root.bind("<Return>", add)

root.mainloop()