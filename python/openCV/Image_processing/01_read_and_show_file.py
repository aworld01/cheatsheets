"""
pip install opencv-python: to install opencv

img = cv2.imread(path) #to read file.
cv2.imshow("Image window", img) #cv2.imshow("Title", object)  to show image
cv2.waitKey(3000) #to hold window for 3 seconds (3000miliseconds = 3seconds)
cv2.destroyAllWindows() #to close and free all resources
"""
import cv2

path = "../images/img1.jpg"
img = cv2.imread(path) #to read file.
cv2.imshow("Image window", img) #cv2.imshow("Title", object)  to show image
cv2.waitKey(3000) #to hold window for 3 seconds (3000miliseconds = 3seconds)
cv2.destroyAllWindows() #to close and free all resources