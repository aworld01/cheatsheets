from tkinter import*

def change():
    data = f"You have selected: {gender.get()}"
    lbl.config(text=data)

root = Tk()
root.title("Radio button")
root.geometry("400x300+500+100")
root.resizable(0,0)

gender = IntVar() #required for Radiobuttons
rbt1 = Radiobutton(root, text="Male", value=0, variable=gender, command=change).grid(row=0, column=0, padx=(120, 0), pady=20)
rbt2 = Radiobutton(root, text="Female", value=1, variable=gender, command=change).grid(row=0, column=1)

lbl = Label(root)
lbl.grid(row=1, column=0, columnspan=2, padx=(120, 0))

root.mainloop()