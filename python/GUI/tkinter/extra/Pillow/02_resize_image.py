"""
img.thumbnail(new_size):-
It maintains the aspect ratio of image.
It can't makes bigger image than it's original size.

new = img.resize((300, 200), Image.ANTIALIAS) #to resize (you can do anything with this)
Image.ANTIALIAS: to make image edge smooth
"""
from PIL import Image

img = Image.open("images/a.jpg")
print(img.size)

# new_size = (1000, 200) #to give new size of image
# img.thumbnail(new_size) #to resize
# print(img.size)


# new = img.resize((200, 200)) #to resize

new2 = img.resize((200, 200), Image.ANTIALIAS) #Image.ANTIALIAS: to make image edge smooth
print(new2.size)