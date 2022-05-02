# x=1
# def show():
#     global x
#     x+=1
#     if (x%2==0):
#         print("Ram")
#     else:
#         print("Rahim")
# show()
# show()
# show()
# show()


from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = '../images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

x=1
def show(e):
    global x
    x+=1
    if (x%2==0):
        root.config(bg="red")
    else:
        root.config(bg='green')

b1 = Button(root, text="Red",font=("times new roman",15,"bold"),bg="red",fg="white",activebackground="blue",activeforeground="red",cursor="hand2")
b1.bind('<Button>', show)
b1.bind('<ButtonRelease>', show)
b1.place(x=10,y=40,width=150,height=28)


root.mainloop()