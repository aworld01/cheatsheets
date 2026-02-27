"""
cap = cv2.VideoCapture(0) #to capture from built-in camera
cap = cv2.VideoCapture(1) #to capture from external camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #to overcome any warning that may come in python3.8 version

Similar
k = cv2.waitKey(25)
if k == ord("q"):
    break

if cv2.waitKey(1) & 0xFF == ord("q"):
    break
"""
import cv2

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700, 450))
        cv2.imshow("Original",frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()