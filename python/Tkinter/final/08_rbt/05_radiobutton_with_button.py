from tkinter import*

def change():
        lbl.config(text=f"You have selected: {gender.get()}")

root = Tk()
root.title("Radio button")
root.geometry("400x300+500+100")
root.resizable(0,0)

gender = StringVar() #required for Radiobuttons
gender.set("female") #to set default selected value

rbt1 = Radiobutton(root, text="Male", value="male", variable=gender).grid(row=0, column=0, padx=(120, 0), pady=20)
rbt2 = Radiobutton(root, text="Female", value="female", variable=gender).grid(row=0, column=1)

lbl = Label(root)
lbl.grid(row=1, column=0, columnspan=2, padx=(120, 0))

btn = Button(root, text="Click", command=change).grid(row=2, column=0, columnspan=2, padx=(120, 0), pady=(20, 0))

root.mainloop()