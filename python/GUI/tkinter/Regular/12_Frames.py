"""
Types of Frames:- 
Frame
LabelFrame
"""
from tkinter import*

root = Tk()
root.title("Tkinter")
root.geometry("1100x600+150+20")
root.resizable(False,False)
root.config(bg="#262626")

"""defining a simple Frame"""
window1 = Frame(root,bg="lightgray",bd=10,relief=GROOVE)
window1.place(x=50,y=50,width=450,height=340)
"""defining Buttons"""
Button(window1,text="Button-1").place(x=50,y=50)
Button(window1,text="Button-2").place(x=250,y=50)
Button(window1,text="Button-3").place(x=50,y=150)

"""defining a LabelFrame"""
window2 = LabelFrame(root,text="StudentDetails",bg="lightgray",bd=10,relief=GROOVE)
window2.place(x=550,y=50,width=450,height=340)
"""defining Buttons"""
Button(window2,text="Button-1").place(x=50,y=50)
Button(window2,text="Button-2").place(x=250,y=50)
Button(window2,text="Button-3").place(x=50,y=150)

root.mainloop()