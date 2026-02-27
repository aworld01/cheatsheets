from tkinter import*
"""
def datafetch():
    x = lbx.get(ACTIVE)
    print('You selected:', x)
def show():
    get_cursor = lbx.curselection() #to get all cursor selected data in tuple.
    for i in get_cursor:
        lbx.delete(get_cursor)

btn = Button(root, text="DELETE", command=show).place(x=20,y=320)
btn2 = Button(root, text = 'SELECT', command=datafetch).place(x=20, y=360)
"""
"""define functions"""
def datafetch():
    x = lbx.get(ACTIVE)
    print('You selected by ACTIVE:', x)
def show_index():
    x = lbx.curselection()
    print('You selected by curselection:', x)
def delete():
    get_cursor = lbx.curselection() #to get all cursor selected index in tuple.
    for i in get_cursor:
        lbx.delete(get_cursor)

root = Tk()
root.title("Home")
root.geometry("700x400+1820+0") #root.geometry("widthxheight+x_pos+y_pos)
root.resizable(0,0)
root.config(bg="gray") #to change background-color
"""frame"""
frm = Frame(root, bg="#1d1d1d")
frm.place(x=20, y=20, relwidth=.60, relheight=.9)
"""List box"""
lbx = Listbox(frm,justify=CENTER,selectmode=EXTENDED)
lbx.place(relheight=1, relwidth=1)
"""insert data with for loop"""
for i in range(50):
    lbx.insert(i,'This is index-'+str(i+1))
"""Scrollbar"""
scrollbar = Scrollbar(frm)
scrollbar.pack(side=RIGHT, fill=Y)
lbx.config(yscrollcommand=scrollbar.set) #to configure listbox
scrollbar.config(command=lbx.yview) #to configure scrollbar
"""Define a button"""
Button(root,text="DELETE", command=delete).place(x=600, y=260)
Button(root, text = 'INDEX', command=show_index).place(x=600, y=300)
Button(root, text = 'DATA', command=datafetch).place(x=600, y=340)

root.mainloop()