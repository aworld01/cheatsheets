"""
img = cv2.resize(img, (600,400)) #img = cv2.resize(object, (width, height)) to resize image
"""
import cv2

path = "../images/img1.jpg"
img = cv2.imread(path)
img = cv2.resize(img, (500, 400)) #to resize image
cv2.imshow("Image window", img)
k = cv2.waitKey()
if k == ord("q"):
    cv2.destroyAllWindows()