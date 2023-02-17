from tkinter import*
"""defining function"""
# def get_data():
#     if chk_var.get() == 1:
#         lbl["text"] = "Check box is ON"
#     else:
#         lbl["text"] = "Check box is OFF"

"""example-2"""
def get_data():
    if chk_var.get() == "On":
        lbl["text"] = "Check box is ON"
    else:
        lbl["text"] = "Check box is OFF"

root = Tk()
root.title("Tkinter")
root.geometry("800x500+200+80")
root.resizable(False,False)

"""defining Checkbutton"""
# chk_var = IntVar()
# chk_var.set(0)
# chk = Checkbutton(root,text="Accept/Not?",onvalue=1,offvalue=0,variable=chk_var).pack(pady=10)

chk_var = StringVar()
chk_var.set("Off")
chk = Checkbutton(root,text="Accept/Not?",onvalue="On",offvalue="Off",variable=chk_var).pack()

"""defining Button"""
btn = Button(root,text="SHOW",command=get_data).pack(pady=10)
"""defining Label"""
lbl = Label(root, text="example")
lbl.pack()

root.mainloop()