"""
Install "IP Webcam" into your mobile.
Open app and click at: Start server
Open your pc Browser and put IP address there (that is in your mobile app) Enter.
Click on Javascript

camera = "http://192.168.100.232:8080/video" #to get video from IP
cap.open(camera) #to open camera
1:36:40
"""
import cv2

camera = "http://192.168.100.232:8080/video"
cap = cv2.VideoCapture(0)
cap.open(camera) #to open camera
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700, 450))
        cv2.imshow("Original",frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()