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
def pink(b):
    root.config(bg="pink")

root.bind("<F1>", red) #on pressing 'F1' function key
root.bind("<F2>", yellow) #on pressing 'F2' function key
root.bind("<F3>", blue) #on pressing 'F3' function key
root.bind("<Delete>", pink) #on pressing 'F3' function key


root.mainloop()