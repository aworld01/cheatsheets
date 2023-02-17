from tkinter import*
"""defining functions"""
"""example-1"""
def show():
    btn.config(text='Come')

"""example-2"""
# def show():
#     btn["text"] = "Hello world!"

root = Tk()
root.title("Home")
root.geometry("500x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")
"""defining Button"""
btn = Button(root, text="Go", command=show)
btn.pack(pady=20)

root.mainloop()