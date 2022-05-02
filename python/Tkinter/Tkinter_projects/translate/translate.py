from tkinter import*
from turtle import width
import dbhelper

"""functions"""
def populate():
    lbx.delete(0, END)
    for rows in dbhelper.show():
        lbx.insert(END, rows[1])
def clear():
    translated.config(text="")
    usr_input.delete(1, END)
def search():
    data = usr_input.get().capitalize()
    for records in dbhelper.where(data):
        if data in records:
            translated.config(text=records[2])
    translated.after(100, search)
def records():
    cnt = f"Total: {dbhelper.count1()}"
    total.config(text=cnt)

root = Tk()
root.title("Translator")
root.geometry("840x540+1820+0")
root.config(bg="maroon")
root.resizable(0,0)
pt = PhotoImage(file = 'icon.png')
root.iconphoto(False, pt)

main = Frame(root, bg="maroon")
main.pack()

Label(main, text="ARTIFICIALWORLD01", font=("Arial",30, "bold")).grid(row=0, column=0, pady=(20, 10))

total = Label(main, text="Total: ")
total.grid(row=1, column=0)
records()

Label(main, text="TRANSLATE", bg="maroon", fg="white").grid(row=2, column=0, sticky=W)

usr_input = Entry(main, font=("arial", 16, "bold"))
usr_input.grid(row=3, column=0, sticky=W, pady=(0, 10), ipadx=283)

Label(main, text="TRANSLATED",bg="maroon", fg="white").grid(row=4, column=0, sticky=W)

translated = Label(main, width=54, bg="gray", font=("Arial",20, "bold"))
translated.grid(row=5, column=0, sticky=W, pady=(0, 10))

Label(main, text="LIST", bg="maroon", fg="white").grid(row=6, column=0, sticky=W)

"""defining a Frame"""
frm_list = Frame(root,bd=2,relief=RIDGE)
frm_list.pack(ipadx=400, ipady=100) #width=800, height=230

"""defining a Listbox"""
lbx = Listbox(frm_list,justify=CENTER,font=("arial", 18, "bold"))
lbx.place(x=0, y=0, relwidth=1, relheight=1)

"""defining a Scrollbar"""
scroll = Scrollbar(frm_list,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)

"""to configure scrollbar with listbox"""
lbx.config(yscrollcommand=scroll.set)
scroll.config(command=lbx.yview)
populate()

"""Buttons"""
frm_btn = Frame(root, bg="maroon")
frm_btn.pack()
clear = Button(frm_btn, text="CLEAR", command=clear).grid(row=0, column=0, pady=10, padx=(0, 10))
close = Button(frm_btn, text="CLOSE", command=root.destroy).grid(row=0, column=1)

# root.bind("<Return>", search)
search()

root.mainloop()