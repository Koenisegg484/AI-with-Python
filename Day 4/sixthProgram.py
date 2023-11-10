import cv2
import time
cam = cv2.VideoCapture(1)
time.sleep(2)
while True:
    _,img = cam.read()
    cv2.imshow("Camera Feed", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()