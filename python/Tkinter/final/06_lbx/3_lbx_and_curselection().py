from tkinter import*
"""
def show():
    get_cursor = lbx.curselection() #to get all cursor selected data in tuple.
    for i in get_cursor:
        print(lbx.get(i))
btn = Button(root,text="SHOW", command=show).place(x=20,y=320)
"""
def show():
    get_cursor = lbx.curselection() #to get all cursor selected data in tuple.
    for i in get_cursor:
        print(lbx.get(i))
        
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
"""get selected data"""
get_cursor = lbx.curselection() #to get all cursor selected data in tuple.
for i in get_cursor:
        print(lbx.get(i))
"""insert data with for loop"""
for i in range(50):
    lbx.insert(i,'This is index-'+str(i+1))
"""Scrollbar"""
scrollbar = Scrollbar(frm)
scrollbar.pack(side=RIGHT, fill=Y)
lbx.config(yscrollcommand=scrollbar.set) #to configure listbox
scrollbar.config(command=lbx.yview) #to configure scrollbar
"""Define a button"""
Button(root,text="SHOW", command=show).place(x=600, y=300)

root.mainloop()