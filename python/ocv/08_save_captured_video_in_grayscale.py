"""
0 is to inform output that coming frame is grayscale
output = cv2.VideoWriter("/home/thor/Videos/output.avi", fourcc, 20.0, (640, 480),0)

gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #to convert into grayscale

output.write(gray) #to save file
1:26:35
"""
import cv2

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("/home/thor/Videos/output.avi", fourcc, 20.0, (640, 480),0)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #to convert into grayscale
        cv2.imshow("Gray",gray)
        output.write(gray) #to save file
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
output.release()
cv2.destroyAllWindows()