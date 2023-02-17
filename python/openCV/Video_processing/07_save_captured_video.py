"""
DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID") 

It contain 4 parameters: name, codec, fps, resolution
output = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480),0)

output.write(frame) #to save file

1:25:35
"""
import cv2

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("/home/thor/Videos/output.avi", fourcc, 20.0, (640, 480))

path = "/home/thor/Videos/holi_song.mp4"
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Original",frame)
        output.write(frame) #to save file
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
output.release()
cv2.destroyAllWindows()