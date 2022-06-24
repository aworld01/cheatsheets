from tkinter import*

"""function"""
def show(event):
    """example-1"""
    # print(event)
    """example-2"""
    if event.keysym == "Delete":
        root.quit()
    else:
        print(event.char)

root = Tk()
root.title("")
root.geometry("600x400")

"""key bindings"""
root.bind("<Key>", show)

root.mainloop()