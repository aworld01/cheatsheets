from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = '../images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def red(r):
    root.config(bg="red")
def yellow(y):
    root.config(bg="yellow")
def blue(b):
    root.config(bg="blue")

root.bind("<Key-a>", red) #on pressing 'a'
root.bind("<Key-b>", yellow) #on pressing 'b'
root.bind("<Key-c>", blue) #on pressing 'c'

root.bind("<Key-A>", red) #on pressing 'A'
root.bind("<Key-B>", yellow) #on pressing 'B'
root.bind("<Key-C>", blue) #on pressing 'C'


root.mainloop()