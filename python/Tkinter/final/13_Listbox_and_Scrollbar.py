from tkinter import*

root = Tk()
root.title("Tkinter")
root.geometry("800x500+250+20")
root.resizable(False,False)
root.config(bg="#262626")

"""defining a Frame"""
frm = Frame(root,bd=2,relief=RIDGE)
frm.place(x=200,y=50,width=400,height=400)

"""defining a Listbox"""
lbx = Listbox(frm,justify=CENTER)
lbx.place(x=0, y=0, relwidth=1, relheight=1)

"""defining a Scrollbar"""
scroll = Scrollbar(frm,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)

"""to configure scrollbar with listbox"""
lbx.config(yscrollcommand=scroll.set)
scroll.config(command=lbx.yview)

"""to add items"""
for i in range(0,101):
    lbx.insert(i,"Data: "+str(i))


root.mainloop()