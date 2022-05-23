'''
from_=50: to define starting value
to=250: to define ending value
length=700: to define full value

orient=VERTICAL (default): to define orientation
orient=HORIZONTAL

width=700 (place.)
sliderlength=100: to define slider length.
showvalue=FALSE: to disable showvalue
'''
from tkinter import*
"""defining function"""
def get_price(price_):
    data = str(price_)
    result.config(text=data)

root = Tk()
root.title("Tkinter")
root.geometry("800x500+200+50")
root.resizable(False,False)
root.config(bg="#262626")
"""defining Scale"""
price = Scale(root,orient=HORIZONTAL,from_=50,to=250,length=700,showvalue=FALSE,command=get_price)
price.pack(pady=10)
result = Label(root,bg="#262626",fg="white")
result.pack()

root.mainloop()