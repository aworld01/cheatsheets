'''
You can't change fg and bg color in comboBox property
state="readonly": to disable editing.
justify=CENTER: to centerized Combobox items.
language.current(0): to select "2nd index's item" by default.
language.set("Select languages"): to give 'select languages' hints.
'''
from tkinter import*
from tkinter import ttk
"""defining function"""
def get_data():
    data = language.get()
    lbl.config(text="You have selected "+data)

root = Tk()
root.title("Tkinter")
root.geometry("800x500+200+80")
root.resizable(False,False)
"""defining a Combobox"""
language = ttk.Combobox(root,values=("HTML","CSS","PHP","Python","Flask"),state="readonly",justify=CENTER)
language.pack(pady=10)
# language.set("Select languages") #to give 'select languages' hints.

language.current(2) #to select "2nd index's item" by default.

"""defining Button"""
btn = Button(root, text="SHOW",command=get_data).pack(pady=10)
"""defining a Label"""
lbl = Label(root, text="Testing")
lbl.pack()

root.mainloop()