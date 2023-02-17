from tkinter import*
"""
lbx.insert(END, "Hello") #to insert data at the end.
lbx.place(relheight=1, relwidth=1)
scrollbar.pack(side=RIGHT, fill=Y)
lbx.config(yscrollcommand=scrollbar.set) #to configure listbox
scrollbar.config(command=lbx.yview) #to configure scrollbar
"""
root = Tk()
root.title("Home")
root.geometry("700x400+1820+0") #root.geometry("widthxheight+x_pos+y_pos)
root.resizable(0,0)
root.config(bg="gray") #to change background-color
"""frame"""
frm = Frame(root, bg="#1d1d1d")
frm.place(x=20, y=20, relwidth=.60, relheight=.9)
"""List box"""
lbx = Listbox(frm)
lbx.place(relheight=1, relwidth=1)

# lbx.insert(END, "Hello") #lbx.insert(index,data)
# lbx.insert(END, "World")

"""insert data with for loop"""
for i in range(50):
    lbx.insert(i,'This is index-'+str(i+1))
"""Scrollbar"""
scrollbar = Scrollbar(frm)
scrollbar.pack(side=RIGHT, fill=Y)
lbx.config(yscrollcommand=scrollbar.set) #to configure listbox
scrollbar.config(command=lbx.yview) #to configure scrollbar

root.mainloop()