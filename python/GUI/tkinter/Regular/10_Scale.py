'''
orient=VERTICAL (default): to define orientation
orient=HORIZONTAL

from_=50: to define starting value
to=250: to define ending value

length=500: to define the length of scale
.pack(ipadx=200): to define the length of scale

sliderlength=100: to define slider length.
showvalue=FALSE: to disable showvalue
'''
# """example-1"""
# from tkinter import*

# """function"""
# def getValue():
#     data = price.get() #returns "Integer" datatype
#     print(data, type(data))

# root = Tk()
# root.title("Tkinter")
# root.geometry("800x500+200+50")
# root.resizable(False,False)
# root.config(bg="#262626")

# """defining Scale"""
# price = Scale(root,orient=HORIZONTAL,from_=50,to=250,length=700,showvalue=FALSE)
# price.pack(pady=10)

# """defining Button"""
# btn = Button(root, text="Click", command=getValue)
# btn.pack()

# root.mainloop()






"""example-2"""
from tkinter import*

"""function"""
def getValue(arg):
    print(arg, type(arg)) #returns "String" datatype

root = Tk()
root.title("Tkinter")
root.geometry("800x500+200+50")
root.resizable(False,False)
root.config(bg="#262626")
"""defining Scale"""
price = Scale(root,orient=HORIZONTAL,from_=50,to=250,length=700,showvalue=FALSE,command=getValue)
price.pack(pady=10)

root.mainloop()