from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = '../images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def green(g):
    root.config(background='green')

def red(g):
    root.config(background='red')

e1 = Entry(root, font=("times new roman", 15))
e1.bind('<FocusIn>', red)
e1.bind('<FocusOut>', green)
e1.place(x=20,y=10)

e2 = Entry(root, font=("times new roman", 15))
e2.place(x=20,y=40)

root.mainloop()