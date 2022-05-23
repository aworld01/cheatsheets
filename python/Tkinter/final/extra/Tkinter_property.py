"""
root.title("Home") #to change the Title

## to change GUI's icon
pt = PhotoImage(file = 'css.png')
root.iconphoto(False, pt)

root.config(bg="gray") #to change window's background-color

root.geometry(widthxheight+x_pos+y_pos)
root.geometry("700x400+1820+0") #to set window (widthxheight) but user can resize it.

## to disable resizing window
root.resizable(width=False,height=False)
root.resizable(False,False)
root.resizable(0,0)

lbl = Label(root,text="This is a Label").place(x=20,y=10) #to apply a label in Tkinter

lbl = Label(root, text="SoftWaves",font=('Arial',15)) #to change font, size of Label

ent = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red").place(x=20,y=70) #with bg="yellow", fg="red"

ent = Entry(root, font=("times new roman", 15, "bold"), bg="yellow", fg="red", show="#").place(x=20,y=100).place(x=20,y=70) #to hide typed text (like password)

b1.bind("<Button-1>", red) #Left_click
b1.bind("<Button-2>", yellow) #Wheel_click
b1.bind("<Button-3>", blue) #Right_click

Button(text="Close", command=root.destroy).pack() #to close app

## to check screen width, height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")
"""