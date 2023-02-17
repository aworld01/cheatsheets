"""
img = cv2.imread(path) #to read file in color mode. (default)
img = cv2.imread(path,1) #to read file in color mode. (default)
img = cv2.imread(path,0) #to read file in gray scale mode.
img = cv2.imread(path,-1) #to read file in color mode. (hd)
"""
import cv2

path = "../images/img1.jpg"
img = cv2.imread(path,-1)
cv2.imshow("Image window", img)
k = cv2.waitKey()
if k == ord("q"):
    cv2.destroyAllWindows() #to close and free all resources