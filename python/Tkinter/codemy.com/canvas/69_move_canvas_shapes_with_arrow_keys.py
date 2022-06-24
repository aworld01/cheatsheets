from tkinter import*

"""functions"""
def left(event):
    x = -10
    y = 0
    canvas.move(circle, x, y)
def right(event):
    x = +10
    y = 0
    canvas.move(circle, x, y)
def up(event):
    x = 0
    y = -10
    canvas.move(circle, x, y)
def down(event):
    x = 0
    y = +10
    canvas.move(circle, x, y)

root = Tk()
root.geometry("800x600")
root.title("")

w = 600
h = 400
x = w//2
y = h//2
"""Canvas"""
canvas = Canvas(root, width=w, height=h, bg="white")
canvas.pack(pady=20)
"""create circle"""
circle = canvas.create_oval(x, y, x+50, y+50, fill="red")
"""bind methods"""
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()