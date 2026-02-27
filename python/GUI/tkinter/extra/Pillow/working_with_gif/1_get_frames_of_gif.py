from PIL import Image
"""get all frames"""
file = Image.open("cortana.gif")
frames = file.n_frames
# print(frames)

"""get all frames one-by-one"""
for item in range(frames):
    print(item)