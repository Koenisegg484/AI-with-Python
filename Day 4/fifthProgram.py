import cv2
import time

vs = cv2.VideoCapture(0)
time.sleep(2)

img = vs.read()[1]
cv2.imshow("Image from Camera", img)
cv2.waitKey(0)
cv2.imwrite("imgFromCamera.jpg", img)
vs.release()