from tkinter import*
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x800")

def animate(count):
    lbl.config(image=framelist[count])
    count += 1
    if count > last_frame:
        count = 0
    root.after(25, lambda : animate(count))

"""global variables"""
framelist = []
frame_index = 0
count = 0

"""count all frames in gif and save into a list"""
file = "cortana.gif"
while True:
    try:
        """read a frame from gif file"""
        part = "gif -index {}".format(frame_index)
        frame = PhotoImage(file=file, format=part)
    except:
        print("break")
        last_frame = frame_index -1 #save index for last frame
        break
    framelist.append(frame)
    print(len(framelist), frame)
    frame_index += 1

"""Label to show gif"""
lbl = Label(root, bg="#202020", image="")
lbl.pack()

"""Button to start"""
start = Button(root, text="Start", command=lambda : animate(0)).pack()

root.mainloop()