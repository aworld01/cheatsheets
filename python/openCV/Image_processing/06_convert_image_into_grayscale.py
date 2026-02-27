"""
cv2.imwrite(dest+"img.jpg", img) #to save image
"""
import cv2

path = "../images/img1.jpg"
dest = "./"
img = cv2.imread(path,0) #to convert into grayscale
cv2.imwrite(dest+"img.jpg", img) #to save image

cv2.waitKey(3000)
cv2.destroyAllWindows()