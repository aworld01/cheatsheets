from tkinter import*
root = Tk()
root.title("Home")
#pt = PhotoImage(file = '../images/css.png')
#root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def red(r):
    root.config(bg="red")
def yellow(y):
    root.config(bg="yellow")
def blue(b):
    root.config(bg="blue")

b1 = Button(root, text="Green",font=("times new roman",15,"bold"),bg="green",fg="white",activebackground="blue",activeforeground="red",cursor="hand2")
b1.bind("<Double-1>", red) #Left_click
b1.bind("<Double-2>", yellow) #Wheel_click
b1.bind("<Double-3>", blue) #Right_click

b1.place(x=10,y=70,width=150,height=28)


root.mainloop()
