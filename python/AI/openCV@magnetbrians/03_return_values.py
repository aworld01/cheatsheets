import cv2

path = "img1.jpg"
img = cv2.imread(path) #returns 3D matrix
img2 = cv2.imread(path,0) #returns 2D matrix

"""to print img matrix"""
# print(img)
# print(img2)

"""to print img type"""
# print(type(img)) #to print type of img
# print(type(img))

"""to print full pixels of image width"""
# print(img[0])

"""to print full length of image width pixels"""
# print(len(img[0]))

"""to print full pixels of image height"""
# print(img[:,0])

"""to print full length of image height pixels)"""
print(len(img[:,0]))



"""1:15:00 / 1:33:05"""