from tkinter import*

root = Tk()
root.title("")
root.geometry("400x500")
# root.iconbitmap('icon.ico')

Button(root, text="Exit", command=root.quit).pack(pady=20)
Button(root, text="Exit2", command=root.destroy).pack()

root.mainloop()