from tkinter import*
from tkinter import messagebox
import wikipedia

"functions"
n = 0
def edit():
    global n
    if n%2==0:
        txt.config(state=NORMAL)
        edt.config(fg="green")
    else:
        txt.config(state=DISABLED)
        edt.config(fg="red")
    n+=1
def clear():
    txt.config(state=NORMAL)
    txt.delete(1.0, END)
    txt.config(state=DISABLED)
def search():
    data = ent.get()
    if data == "":
        messagebox.showinfo("Information", "Search box should not be empty")
    else:
        data = ent.get()
        # fetched_data=wikipedia.summary(data, sentences=10)
        fetched_data=wikipedia.summary(data)
        txt.config(state=NORMAL)
        txt.delete(1.0, END)
        txt.insert(1.0, fetched_data)
        txt.config(state=DISABLED)

root = Tk()
root.title("Search Application")
root.geometry("1350x700+0+0")
root.resizable(0, 0)
root.config(bg="#262626")

Label(root, text="Search Application", font=("times new roman", 40, "bold"), bg="white", fg="#262626").place(x=0, y=0, relwidth=1)

Label(root, text="Search World", font=("times new roman", 30, "bold"), bg="#262626", fg="white").place(x=10, y=100)

ent = Entry(root, font=("times new roman", 20))
ent.place(x=280, y=108, width=570)

Button(root, text="Search", font=("times new roman", 20, "bold"), bg="lightyellow", fg="#262626", command=search).place(x=900, y=108, height=36, width=120)

Button(root, text="Clear", font=("times new roman", 20, "bold"), bg="lightyellow", fg="#262626", command=clear).place(x=1060, y=108, height=36, width=120)

edt = Button(root, text="Edit", font=("times new roman", 20, "bold"), bg="lightyellow", fg="#262626", command=edit)
edt.place(x=1220, y=108, height=36, width=120)

frm = Frame(root, bd=2, relief=RIDGE)
frm.place(x=10, y=170, width=1330, height=520)

scroll = Scrollbar(frm, orient=VERTICAL)
scroll.pack(side=RIGHT, fill=Y)

txt = Text(frm, font=("times new roman", 15), state=DISABLED,yscrollcommand=scroll.set)
txt.pack(fill=BOTH, expand=1)

scroll.config(command=txt.yview)

root.mainloop()