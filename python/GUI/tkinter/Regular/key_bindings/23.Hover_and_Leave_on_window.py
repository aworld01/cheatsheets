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

root.bind("<Enter>", red) #on Hover
root.bind("<Leave>", yellow) #on Leave


root.mainloop()