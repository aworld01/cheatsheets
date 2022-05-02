"""
frame2 = cv2.flip(frame, 0) #rotate at down
frame2 = cv2.flip(frame, 1) #rotate left to right
1:27:20
"""
import cv2

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700, 450))
        frame2 = cv2.flip(frame, 1) #rotate left to right
        cv2.imshow("Original",frame)
        cv2.imshow("Fliped",frame2)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()