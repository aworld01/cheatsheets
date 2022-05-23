"""
img = cv2.imread(path) #to read file.
img = cv2.imread(path,1) #to read file in color mode (default)
img = cv2.imread(path,0) #to read file in gray scale mode
img = cv2.imread(path,-1) #to read file in color mode (hd)
cv2.imshow("Original", img) #to show image / cv2.imshow("Title", object)
img = cv2.resize(img, (600,400)) #to resize image / img = cv2.resize(object, (width, height))

cv2.waitKey() #to hold window for display / cv2.waitKey(0) default
cv2.waitKey(3000) #to hold window for 3 seconds (3000miliseconds = 3seconds)
cv2.destroyAllWindows() #to close and free all resources
"""
import cv2 #pip install opencv-python

path = "images/img1.jpg"
"""color image"""
# img = cv2.imread(path,1) #to read file
# # print(img) #to print data in array
# img = cv2.resize(img, (600,400)) #to resize image(width, height)
# cv2.imshow("Original", img) #to show image
"""gray scale image"""
img2 = cv2.imread(path,0) #to read file
print(img2) #to print data in array
img2 = cv2.resize(img2, (600,400)) #to resize image(width, height)
cv2.imshow("Grayscale Image", img2) #to show image / cv2.imshow("Title", object)

k = cv2.waitKey() #to hold window for display
if k == ord("q"):
    cv2.destroyAllWindows() #to close and free all resources