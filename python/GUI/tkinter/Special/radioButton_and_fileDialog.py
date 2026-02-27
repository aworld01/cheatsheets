from tkinter import*
from tkinter import filedialog

"""function"""
def select():
    if selected.get() == 0:
        select_file = filedialog.askopenfile(title="Select file").name
        path_str.set(select_file)
    else:
        select_folder = filedialog.askdirectory(title="Select folder")
        path_str.set(select_folder)

root = Tk()
root.title("radioButton_&_fileDialog")
root.geometry("500x400+500+10")

"""Entry"""
path_str = StringVar()
path_ent = Entry(root, textvariable=path_str)
path_ent.place(x=10, y=310, width=402)

"""Button"""
path_btn = Button(root, text="Select", command=select)
path_btn.place(x=425, y=310)

"""Radiobuttons"""
selected = IntVar()
rbt1 = Radiobutton(root, text="File", value=0, variable=selected)
rbt1.place(x=10, y=50)
rbt2 = Radiobutton(root, text="Folder", value=1, variable=selected)
rbt2.place(x=100, y=50)

root.mainloop()