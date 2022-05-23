from tkinter import*

root = Tk()
root.title("Home")
root.geometry("400x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def show():
    a = int(x.get())
    result = []
    for i in range(1,11):
        result.append(a*i)
    lbl.config(text=result, bg="gray")


x = StringVar()
"""Entry"""
ent = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", textvariable=x)
ent.pack(pady=10)
"""Button"""
btn = Button(root, text="Go",bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=show)
btn.pack(pady=10)
"""Label"""
lbl = Label(root, bg="#262626")
lbl.pack(pady=10)

root.mainloop()