"""
PATH
====
Relative path:
    path = "./img4.jpg" #parentFolder
    child_path = "./childFolder/img1.jpg" #childFolder
    path = "../img4.jpg" #to go back and select "img4.jpg" file ("../" to 1step back)
Absolute path:
    path = "C:\\Users\\Abdul\\Desktop\\new\\openCV@magnetbrians\\images\\parentFolder\\img4.jpg"
img = cv2.imread(path, flag) (flag = 1 is default)
example:
    img = cv2.imread("image1.jpg")
    img = cv2.imread("image1.jpg", 1)
    img = cv2.imread("image1.jpg", 0)
    img = cv2.imread("image1.jpg", -1)
FLAG
====
1 = cv2.IMREAD_COLOR (default)
0 = cv2.IMREAD_GRAYSCALE
-1 = cv2.IMREAD_UNCHANGED
example:
    img = cv2.imread("image1.jpg")
    img = cv2.imread("image1.jpg", cv2.IMREAD_COLOR)
    img = cv2.imread("image1.jpg", cv2.IMREAD_GRAYSCALE)
    img = cv2.imread("image1.jpg", cv2.IMREAD_UNCHANGED)
"""
import cv2

path = "./img1.jpg"
flag = "1" #(default)

img = cv2.imread(path) #to read file (it returns a matrix)

print(img)

"""43:00 / 1:33:05"""