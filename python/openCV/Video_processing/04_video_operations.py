"""
cap = cv2.VideoCapture(path) #it returns values in object form

frame = cv2.resize(frame,(700, 450)) #frame = cv2.resize(frame, (width, height)) #to resize window

cv2.imshow("Video-1",gray) #to show gray video

k = cv2.waitKey(25) #to handle playback speed (more greater more show)

To stop
k = cv2.waitKey(25)
if k == ord("q"):
        break

To overcome any forther problem
k = cv2.waitKey(25)
if k == ord("q") & 0xFF:
        break
"""
import cv2

path = "test.mp4"
cap = cv2.VideoCapture(path)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(700, 450))
    cv2.imshow("Video-1", frame)
    k = cv2.waitKey(25) #to handle playback speed
    if k == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()