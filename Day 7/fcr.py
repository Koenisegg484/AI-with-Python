import os
import cv2

dataset = 'dataset'

name = input("Enter the name of the user : ")

if not os.path.isdir(dataset):
    os.mkdir(dataset)
pathn = os.path.join(dataset, name)
if not os.path.isdir(pathn):
    os.mkdir(pathn)

count = 1


alg = "haarcascade_frontalface_default.xml"
haar = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(1)

while True:
    nun, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = haar.detectMultiScale(gray, 1.3, 4)

    if count < 41:
        for (x,y,w,h) in face:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 0), 2)
            faceOnly = gray[y:y+h, x:x+w]
            rszd = cv2.resize(faceOnly, (100,100))
            filename = f"{pathn}/{name}{count}.png"
            cv2.imwrite(filename, rszd)
            count+=1
    if count > 41:
        cv2.imshow("Faces detected", img)
    else:
        cv2.imshow("Detecting Faces", img)
    key = cv2.waitKey(10)
    if key == ord("q") and count > 31:
        break

cam.release()
cv2.destroyAllWindows()