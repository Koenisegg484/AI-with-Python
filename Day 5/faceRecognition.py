import cv2
import os
# import time

dataset = "dataset"
name = "allFaces"

if not os.path.isdir(dataset):
    os.mkdir(dataset)
pathn = os.path.join(dataset, name)
if not os.path.isdir(pathn):
    os.mkdir(pathn)

(width, height) = (130, 100)
alg = "haarcascade_frontalface_default.xml"
haar = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(1)
count = 1

while count < 31:
    _,img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = haar.detectMultiScale(gray, 1.3, 4)
    for(x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0, 255), 2)
        faceOnly = gray[y:y+h, x:x+w]
        resized = cv2.resize(faceOnly, (width, height))
        filename = f"{pathn}/test{count}.jpg"
        cv2.imwrite(filename, resized)
        count += 1
        # time.sleep(1.5)
    cv2.imshow("Face Recognition", img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
