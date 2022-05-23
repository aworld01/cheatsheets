"""ent.delete(0, END)"""
def click():
    data = ent.get()
    lbl.config(text=f"Hello {data} darling how are you?")
    ent.delete(0, END)

from tkinter import*

root = Tk()
root.title("Home")
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

"""assign a entry"""
ent = Entry(root)
ent.pack(pady=20)
"""assign a button"""
btn = Button(root, text="Go", command=click)
btn.pack(pady=20)
"""assign a label"""
lbl = Label(root, bg="gray")
lbl.pack(pady=20)



root.mainloop()