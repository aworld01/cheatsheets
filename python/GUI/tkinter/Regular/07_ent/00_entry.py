from tkinter import*
"""
font=('times new roman', 15)
font=('times new roman', 15, 'bold')
font=('times new roman', 15, 'italic bold')
bg='yellow'
fg='red'
relief=SUNKEN (SUNKEN, GROOVE, RAISED)
bd=2
width=150, height=200
show="*": to hide text with '*' symbol
"""
root = Tk()
root.title("Home")
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

"""assign a entry"""
Entry(root, font=('times new roman', 15, 'italic bold')).place(x=20, y=20)
Entry(root, show="*").place(x=20, y=60)

root.mainloop()