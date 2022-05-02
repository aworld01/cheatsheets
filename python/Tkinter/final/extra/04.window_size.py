# from tkinter import*

# root = Tk()
# root.title("Home")
# pt = PhotoImage(file = 'images/css.png')
# root.iconphoto(False, pt)
# root.config(bg="green")
# root.minsize(600,300) #to set minimum size of window
# root.maxsize(800,400) #to set maximum size of window

# root.mainloop()




# from tkinter import*

# root = Tk()
# root.title("Home")
# pt = PhotoImage(file = 'images/css.png')
# root.iconphoto(False, pt)
# root.config(bg="green")
# root.geometry("700x400+1820+0") #to set (widthxheight) but user can resize it. (1820+0) is window's opening position.

# root.mainloop()




# from tkinter import*

# root = Tk()
# root.title("Home")
# pt = PhotoImage(file = 'images/css.png')
# root.iconphoto(False, pt)
# root.config(bg="green")
# root.geometry("700x400+1820+0")
"""to disable resize window"""
# # root.resizable(width=False,height=False)
# # root.resizable(False,False)
# # root.resizable(0,0)

# root.mainloop()





from tkinter import*

root = Tk()
root.title("Home")
root.config(bg="olivedrab1")
"""set size of windows"""
root.geometry("500x600+1820+0")
root.minsize(500,600) #to set minimum size of window
"""to set maximum size of window"""
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.maxsize(width, height)

root.mainloop()