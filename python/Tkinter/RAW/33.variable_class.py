from tkinter import*
root = Tk()
root.title("Home")
root.geometry("1000x400+1820+0")
root.resizable(0,0)
root.config(bg="#262626")

# def age():
#     data1 = en1.get()
#     data2 = en2.get()
#     result.config(text=f'Hello {(data1)} Your age is: {(data2)}')

def write():
    data = en1.get()
    data2 = en2.get()
    result.config(text=(data)+(data2))

# en1 = StringVar()
# en2 = IntVar()

en1 = IntVar()
en2 = IntVar()

e1 = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", textvariable=en1)
e1.place(x=10,y=10, width=150,height=28)

e2 = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", textvariable=en2)
e2.place(x=10,y=40, width=150,height=28)

b1 = Button(root, text="Show",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="blue",activeforeground="red",cursor="hand2", command=write).place(x=10,y=70,width=150,height=28)

result = Label(root,font=("times new roman",25,"bold"),bg="#262626",fg="white")
result.place(x=10,y=130)

root.mainloop()