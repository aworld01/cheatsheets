from tkinter import*
from PIL import Image, ImageTk

root = Tk()
root.geometry("600x400")

file = "cortana.gif"
img = Image.open(file)
ima = img.resize((300, 300), Image.ANTIALIAS)
frames = img.n_frames #to get frames of gif
print(frames)

# im = [PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)] #to store all PhotoImage objects into im

root.mainloop()