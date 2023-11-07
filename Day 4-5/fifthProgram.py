import cv2
import time.sleep

vs = cv2.VideoCapture(0)
sleep(2)

_,img = vs.read()
cv2.imwrite("imgFromCamera.jpg", img)
vs.release()
