"""
img = cv2.flip(img, 0) #
img = cv2.flip(img, 1) #
img = cv2.flip(img, -1) #
"""
import cv2

path = "../images/img1.jpg"
img = cv2.imread(path)
img = cv2.resize(img, (600,400))
cv2.imshow("Original", img)

"""flip image"""
img2 = cv2.imread(path)
img2 = cv2.resize(img2, (600,400))
img2 = cv2.flip(img2, 0) #to flip
cv2.imshow("Fliped Image", img2)

cv2.waitKey(10000)
cv2.destroyAllWindows()