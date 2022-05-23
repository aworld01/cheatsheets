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
def green(r):
    root.config(bg="green")
def maroon(y):
    root.config(bg="maroon")

root.bind("<A>", red) #on pressing 'A' key
root.bind("<a>", yellow) #on pressing 'a' key
root.bind("<B>", blue) #on pressing 'B' key
root.bind("1", pink) #on pressing '1' numeric key
root.bind("2", green) #on pressing '2' numeric key
root.bind("3", maroon) #on pressing '3' function key


root.mainloop()