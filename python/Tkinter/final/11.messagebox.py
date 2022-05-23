"""
showerror
showinfo
showwarning
"""
from tkinter import*
from tkinter import messagebox
"""defining functions"""
def error():
    messagebox.showerror("Error","This is an error messageBox...")
def info():
    messagebox.showinfo("Information","This is an information messageBox...")
def warning():
    messagebox.showwarning("Warning","This is a warning messageBox...")

root = Tk()
root.title("Tkinter")
root.geometry("800x500+250+50")
root.config(bg="#262626")
root.resizable(False,False)
"""defining Buttons"""
btn1 = Button(root,text="Error",command=error).pack(pady=10)
btn2 = Button(root,text="Information",command=info).pack(pady=10)
btn3 = Button(root,text="Warning",command=warning).pack()

root.mainloop()