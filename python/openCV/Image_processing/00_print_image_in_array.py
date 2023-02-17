"""
img = cv2.resize(img, (600,400)) #img = cv2.resize(object, (width, height)) to resize image
"""
import cv2

path = "../images/img1.jpg"
"""for grayscale image"""
# img = cv2.imread(path,0) #to read file in grayscale mode.
# print(img)

"""for color image"""
img = cv2.imread(path) #to read file in color mode.
print(img)