from PIL import Image

img1 = Image.open("images/a.jpg")
img2 = Image.open("images/star.png")
img2 = img2.resize((100, 100), Image.ANTIALIAS) #to resize image
print(img1.size)
print(img2.size)
img = img1.copy()
img.paste(img2, (120, 110))
img.save("New.jpg")