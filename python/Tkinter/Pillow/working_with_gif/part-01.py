from tkinter import*
from PIL import Image, ImageTk

root = Tk()
root.geometry("600x400")

file = "cortana.gif"
img = Image.open(file)
frames = img.n_frames #to get frames of gif
# print(frames)

im = [PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)] #to store all PhotoImage objects into im

for item in range(frames):
    print(item)

"""to iterate frames"""
anim = None
count = 0
def animation(count):
    global anim
    im2 = im[count]
    lbl.config(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda:animation(count))
def stop():
    global anim
    root.after_cancel(anim)


"""Label"""
lbl = Label(root, bg="white")
lbl.pack()

start = Button(root, text="Start", command=lambda:animation(count))
start.pack()
# stop = Button(root, text="Stop", command=stop)
# stop.pack()

root.mainloop()