'''
relief=SUNKEN (SUNKEN, GROOVE, RAISED)
bd=2: (to give border)
bd=None (to remove border)

activebackground="black": on hover
activeforeground="white": on hover
cursor="hand2": (hand1, hand2)
'''
from tkinter import*

root = Tk()
root.title("Home")
root.geometry("400x600+1820+0")
root.resizable(0,0)
root.config(bg="#262626")
"""defining a Button"""
btn = Button(root, text='Show', activebackground="black", activeforeground="white", cursor="hand2")
btn.pack(pady=20)

root.mainloop()