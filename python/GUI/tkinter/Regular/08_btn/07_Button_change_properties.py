from tkinter import*
"""defining a function"""
"""Example-1"""
# def show():
#     btn["text"] = "Hello world!"
#     btn["bg"] = "black"
#     btn["fg"] = "white"
#     btn["width"] = 30
#     btn["height"] = 10

"""Example-2"""
def show():
    btn.config(text="Hello world", bg="black", fg="white", width=30, height=10)

root = Tk()
root.title("Home")
root.geometry("500x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")
"""defining a Button"""
btn = Button(root, text="Go", command=show)
btn.pack()

root.mainloop()