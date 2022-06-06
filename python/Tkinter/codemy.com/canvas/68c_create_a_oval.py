from tkinter import*

root = Tk()
root.title("")
root.geometry("500x500")

mycanvas = Canvas(root, width=300, height=200, bg="white")
mycanvas.pack(pady=20)

# mycanvas.create_rectangle(50, 150, 250, 50, fill="pink")

"""
mycanvas.create_line(x1, y1, x2, y2, fill="color")
oval: x1, y1 = Top Left
oval: x2, y2 = Bottom Right
"""
mycanvas.create_oval(50, 150, 250, 50, fill="cyan")


# mycanvas.create_line(0, 100, 300, 100)
# mycanvas.create_line(150, 0, 150, 200)

root.mainloop()