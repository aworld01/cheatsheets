from tkinter import *
import dbhelper3
from tkinter import messagebox

def add(event):
    if(len(en.get()) == 0):
        messagebox.showerror('ERROR', 'No data available\nPlease enter some task')
    else:
        dbhelper3.insertdata(en.get())
        en.delete(0, END)
        populate()

def add2():
    if(len(en.get()) == 0):
        messagebox.showerror('ERROR', 'No data available\nPlease enter some task')
    else:
        dbhelper3.insertdata(en.get())
        en.delete(0, END)
        populate()

def populate():
    lbx.delete(0, END)
    for rows in dbhelper3.show():
        lbx.insert(END, rows[1])

def delete(event):
    dbhelper3.deletebytask(lbx.get(ANCHOR)) #ANCHOR means selected
    populate()

root = Tk()
root.title('TODO')
root.geometry('500x600')
root.resizable(0, 0)
root.config(bg='#1d1d1d')

Label(
    root,
    text='Task Manager',
    bg = '#1d1d1d',
    fg = '#eeeeee',
    font=('verdana 20')
).pack(pady=10)

####################################
frame = Frame(
    root,
    bg='#1d1d1d',
).pack()

en = Entry(
    frame,
    font=('verdana'),
    bg = '#eeeeee',
)
en.pack(ipadx=20, ipady=5, pady=5)

btn = Button(
    frame,
    text = 'ADD TASK',
    command = add2,
    bg = '#000000',
    fg = '#eeeeee',
    relief = 'flat',
    font = ('verdana'),
    highlightcolor = '#000000',
    activebackground = '#1d1d1d',
    bd = 0,
    activeforeground = '#eeeeee'
)
btn.pack(padx=20, ipadx=20, ipady=5)

en.bind("<Return>", add)

Label(
    root,
    text='Your Tasks',
    bg='#1d1d1d',
    fg='#eeeeee',
    font=('Calibri', 18)
).pack(pady=10)

taskframe = Frame(
    root,
    # bg='#1d1d1d'
    bg='blue'
)
taskframe.pack(fill=BOTH, expand=300)

scrollbar = Scrollbar(taskframe)
scrollbar.pack(side=RIGHT, fill=Y)

lbx = Listbox(
    taskframe,
    font=('Verdana 18 bold'),
    bg='#1d1d1d',
    fg='#eeeeee',
    selectbackground='#eeeeee', #to change selected item background
    selectforeground='#1d1d1d' #to change selected item foreground
)
lbx.pack(fill=BOTH, expand=300)
lbx.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lbx.yview)
lbx.bind("<Double-Button-1>", delete)
lbx.bind("<Delete>", delete)

populate()

Label(
    root,
    text='TIP: Double click on a Task to delete',
    bg='#1d1d1d',
    fg='#FFEB3B',
    font=('Calibri 18')
).pack(side=BOTTOM, pady=10)

## 23:00/32:29

root.mainloop()