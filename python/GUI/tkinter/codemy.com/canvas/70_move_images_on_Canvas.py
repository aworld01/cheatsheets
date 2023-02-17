from tkinter import*

"""functions"""
def left(event):
    x = -10
    y = 0
    canvas.move(image, x, y)
def right(event):
    x = +10
    y = 0
    canvas.move(image, x, y)
def up(event):
    x = 0
    y = -10
    canvas.move(image, x, y)
def down(event):
    x = 0
    y = +10
    canvas.move(image, x, y)

root = Tk()
root.title("")
root.geometry("800x600")
"""variables"""
w = 600
h = 400
x = w//2
y = h//2
"""Canvas"""
canvas = Canvas(root, width=w, height=h, bg="white")
canvas.pack(pady=20)
"""add image to Canvas"""
img = PhotoImage(file="border.png")
image = canvas.create_image(60,20, anchor=NW, image=img)
"""bind methods"""
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()