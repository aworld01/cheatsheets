from tkinter import*
"""
text='This is a Label'
text='newline\nwithout\nwidth&height'

bg='yellow': Background-color
fg='red': Foreground-color

'''font=("fimily", size, "style")'''
font=('times new roman', 15)
font=('times new roman', 15, 'bold')
font=('times new roman', 15, 'italic bold')
"""
root = Tk()
root.title("Home")
root.geometry("700x400+1820+0")
root.config(bg="gray")

"""assign a label"""
lbl = Label(root, text='This is a Label with new line', font=('times new roman', 15, 'italic bold'))
lbl.place(x=0, y=0)

root.mainloop()
