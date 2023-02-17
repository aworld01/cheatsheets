from tkinter import*
"""
text='This is a Label'
text='newline\nwithout\nwidth&height'

#font=("fimily", size, "style")
font=('times new roman', 15)
font=('times new roman', 15, 'bold')
font=('times new roman', 15, 'italic bold')

bg='yellow': Background-color
fg='red': Foreground-color
padx=20: (to give margin left&right)
pady=20: (to give margin up&down)

relief=SUNKEN (SUNKEN, GROOVE, RAISED)
bd=2: (to give border)

width="15" (approximate 15 charecter)
height="2" (2 lines)

lbl = Label(root, text='This is a Label').place() #You can't change this behavior later

You can change this behavior later
lbl = Label(root, text='This is a Label')
lbl.place(relheight=1)
"""
root = Tk()
root.title("Home")
root.geometry("700x400+1820+0")
root.resizable(0,0)
root.config(bg="gray")

"""assign a label"""
lbl = Label(root, text='This is a Label')
lbl.place(relheight=1)

root.mainloop()