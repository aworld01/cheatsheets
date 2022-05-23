from PIL import Image

"""example-1"""
# file = Image.open("cortana.gif")
# file.seek(0)
# file.save("frames/frame-.png")


"""example-2"""
file = Image.open("image.gif") #to make object of open image
frames = file.n_frames #to get number of frames

for frame in range(frames):
    file.seek(frame)
    file.save(f"frames/frame{frame}.png")