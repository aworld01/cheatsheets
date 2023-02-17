"""
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #to convert into gray
"""
import cv2

path = "test.mp4"
cap = cv2.VideoCapture(path)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(700, 450))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #to convert into grayscale
    cv2.imshow("gray",gray)
    k = cv2.waitKey(25)
    if k == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()