from tkinter import*

root = Tk()
root.title("")
root.geometry("500x500")

mycanvas = Canvas(root, width=300, height=200, bg="white")
mycanvas.pack(pady=20)

"""mycanvas.create_line(x1, y1, x2, y2, fill="color")"""
mycanvas.create_line(0, 100, 300, 100)
mycanvas.create_line(150, 0, 150, 200)

root.mainloop()