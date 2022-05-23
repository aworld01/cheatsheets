from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title("")
root.geometry("400x500")

img = Image.open("images/a.jpg")
image = ImageTk.PhotoImage(img)

lbl = Label(root, image=image)
lbl.pack()

root.mainloop()