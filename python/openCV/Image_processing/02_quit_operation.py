"""
k = cv2.waitKey() #to hold window for display
if k == ord("q"):
    cv2.destroyAllWindows() #to close and free all resources
"""
import cv2

path = "../images/img1.jpg"
img = cv2.imread(path)
cv2.imshow("Image window", img)
k = cv2.waitKey()
"""quit operation"""
if k == ord("q"): #to perform quit opration
    cv2.destroyAllWindows()