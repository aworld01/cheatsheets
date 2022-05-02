'''
"<Control_L><y>": to left_CTRL+L
"<Control_R><b>": to right_CTRL+R
"<Return>": to Enter
'''
"""define functions"""
def red(r):
    root.config(bg="red")
def blue(b):
    root.config(bg="blue")
def yellow(y):
    root.config(bg="yellow")
def green(y):
    root.config(bg="green")
def out(x):
    root.destroy()
    # root.quit()

from tkinter import*

root = Tk()
root.title("Home")
root.geometry("400x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

"""key bindings"""
root.bind("r", red) #r: to red
root.bind("Y", yellow) #Y: to yellow
root.bind("<Control_L><b>", blue) #Control+b: to blue
root.bind("<Control_R><g>", green) #Wright_Control+g: to green
root.bind("<Return>", out) #Enter: to exit

"""define Label"""
lbl = Label(root,text="r: to Red\nY: to Yellow\nCtrl+b: to Blue\nRight_Control+g: to green\nEnter: to exit", font = ('consolas', 14))
lbl.place(x=20, y=20)

"""define button"""
Button(root, text="Exit", command=root.destroy).pack(side=BOTTOM)

root.mainloop()