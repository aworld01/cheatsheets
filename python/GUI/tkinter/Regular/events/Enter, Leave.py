from tkinter import*

def entered(event):
    print("You entered in Frame1...")
def left(event):
    print("You left to Frame1...")

root = Tk()
root.geometry("600x600")
"""Frames"""
frm1 = Frame(root, bg="#000000")
frm1.pack(expand=True, fill=BOTH)
frm1.bind("<Enter>", entered)
frm1.bind("<Leave>", left)

frm2 = Frame(root, bg="#343434")
frm2.pack(expand=True, fill=BOTH)

root.mainloop()