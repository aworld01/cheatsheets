from tkinter import*

def change():
    if gender.get() == 0:
        lbl.config(text="You have selected: Male")
    else:
        lbl.config(text="You have selected: Female")

root = Tk()
root.title("Radio button")
root.geometry("400x300+500+100")
root.resizable(0,0)

gender = IntVar() #required for Radiobuttons
gender.set(1) #to set default selected value

rbt1 = Radiobutton(root, text="Male", value=0, variable=gender, command=change).grid(row=0, column=0, padx=(120, 0), pady=20)
rbt2 = Radiobutton(root, text="Female", value=1, variable=gender, command=change).grid(row=0, column=1)

lbl = Label(root)
lbl.grid(row=1, column=0, columnspan=2, padx=(120, 0))

root.mainloop()