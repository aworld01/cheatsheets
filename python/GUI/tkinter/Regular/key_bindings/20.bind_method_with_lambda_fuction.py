# ## function
# def show(x,y):
#     return x+y
# num = show(10, 5)
# print(num)

# ## anonymous/lambda function
# show2 = lambda x,y:x+y
# num2 = show2(20, 10)
# print(num2)



from tkinter import*
root = Tk()
root.title("Home")
pt = PhotoImage(file = '../images/css.png')
root.iconphoto(False, pt)
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

def red():
    root.config(bg="red")

green = lambda g:root.config(bg="green")

b1 = Button(root, text="Red",font=("times new roman",15,"bold"),bg="red",fg="white",activebackground="blue",activeforeground="red",cursor="hand2")
b1.config(command=red)
b1.place(x=10,y=10,width=150,height=28)

b2 = Button(root, text="Green",font=("times new roman",15,"bold"),bg="green",fg="white",activebackground="blue",activeforeground="red",cursor="hand2")
b2.bind("<Button>", green)
b2.place(x=10,y=40,width=150,height=28)


root.mainloop()