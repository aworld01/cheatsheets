from tkinter import*
"""defining function"""
c=1
def show(b):
    global c
    c += 1
    if (c%2==0):
        if (btn1["text"]==""):
            btn1["text"] = "0"
    else:
        if (btn2["text"]==""):
            btn2["text"] = "X"

root = Tk()
root.title("Home")
root.geometry("500x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")
"""defining Button"""
btn1 = Button(root, command=lambda:show(btn1))
btn1.pack(pady=20)
btn2 = Button(root, command=lambda:show(btn2))
btn2.pack()

root.mainloop()