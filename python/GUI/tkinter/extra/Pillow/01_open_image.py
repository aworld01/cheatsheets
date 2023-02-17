from PIL import Image

img = Image.open("images/a.jpg") #to create an image object

print(img.height) #to get height

print(img.width) #to get width

print(img.size) #to get width, height

print(img.format) #to get fileFormat

print(img.mode) #to get mode

# img.show() #it will show your image in your default image browser.

# img.save("small.jpg") #to save new image with new name