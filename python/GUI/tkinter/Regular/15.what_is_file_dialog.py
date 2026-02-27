"""
FILEDIALOG:-

def select():
    select_folder = filedialog.askdirectory(title="Select folder") #to open popup window to select any folder.
    print(select_folder)

def select():
    select_file = filedialog.askopenfile(title="Select file") #to open popup window to select any file.
    print(select_file) #this will return an object
    print(select_file.name) #to fetch only file path.

def select():
    select_file = filedialog.askopenfilename(title="Select file") #to open popup window to select any file.
    print(select_file)
    print(select_file.split("/")[-1]) #to split only file name.

def select():
    open_file = filedialog.askopenfilenames(title="Select file") #to open popup window to select multiple files in tuple forms.
    print(open_file)

def select():
    open_file = filedialog.askopenfiles(title="Select file") #to open popup window to select multiple files in object format.
    print(open_file)

def select():
    save_file = filedialog.asksaveasfile(title="Select file") #to open popup window to save file.
    print(save_file)

def open():
    save_as = filedialog.asksaveasfile(title="Select file",filetypes=(("Text file:",".txt"),("Others","*"))) #to open popup window to save file.
"""
from tkinter import*
from tkinter import filedialog

root = Tk()
root.title("Tkinter")
root.geometry("800x500+250+20")
root.resizable(False,False)
root.config(bg="#262626")

def select():
    save_file = filedialog.asksaveasfile(title="Select file") #to open popup window to save file.
    print(save_file)

btn = Button(root,text="Open folder",command=select).place(x=50,y=50)

root.mainloop()