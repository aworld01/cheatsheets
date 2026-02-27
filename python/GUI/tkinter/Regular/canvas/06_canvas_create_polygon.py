from tkinter import*

root = Tk()

canvas = Canvas(root, width=800, height=600)
canvas.pack()

points = [250,110, 480,200, 280,280, 250,110]
canvas.create_polygon(points, fill="green", outline="yellow", width=5)

root.mainloop()