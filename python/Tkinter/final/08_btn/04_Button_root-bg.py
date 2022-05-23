from tkinter import*
"""defining functions"""
def red():
    root.config(bg="red")
def green():
    root.config(bg="green")

root = Tk()
root.title("Home")
root.geometry("500x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")
"""difining Buttons"""
btn1 = Button(root, text="Red", command=red)
btn1.pack(pady=20)

btn2 = Button(root, text="Green", command=green)
btn2.pack()

root.mainloop()