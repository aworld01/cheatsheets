'''
command=root.destroy: to close the app.
'''
from tkinter import*
"""defining a function"""
def close():
    root.destroy()

root = Tk()
root.title("Home")
root.geometry("500x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")
"""defining a Button"""
"""Example-1"""
# btn = Button(root, text="Close", command=close)
# btn.pack(pady=50)

"""Example-2"""
btn = Button(root, text="Close", command=root.destroy)
btn.pack(pady=50)

root.mainloop()