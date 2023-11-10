# import cv2
# import imutils
# import time
# cam = cv2.VideoCapture(0)
# time.sleep(2)

# firstFrame = None
# area = 1000

# while True:
#     img = cam.read()[1]
#     text = "Normal"
#     imutils.resize(img, width=500)
#     grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     gaussBlur = cv2.GaussianBlur(grayImg, (21,21), 0)

#     if firstFrame is None:
#         firstFrame = gaussBlur
#         continue
#     imgDiff = cv2.absdiff(firstFrame, gaussBlur)
#     threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
#     threshImg = cv2.dilate(threshImg, None, iterations=2)
#     cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     for c in cnts:
#         if cv2.contourArea(c) < area:
#             continue
#         (x, y, w, h) =  cv2.boundingRect(c)
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)
#         text = "Moving Object Detected"
#         print(text)
#     cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0, 255), 2)

#     cv2.imshow("Camera Feed normal", img)
#     # cv2.imshow("Camera Feed gauss Blur", gaussBlur)
#     # cv2.imshow("Camera Feed threshImg", threshImg)
#     # cv2.imshow("Camera Feed gray img", grayImg)

#     key = cv2.waitKey(1) & 0xFF
#     if key == ord("q"):
#         break

# cam.release()
# cv2.destroyAllWindows()

import cv2, imutils
import time

cam = cv2.VideoCapture(1) ## IP Cam
origImg = None
area = 500
time.sleep(1)  #wait 1 sec for camera

while True:
    _,img = cam.read()
    img = imutils.resize(img, width=500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blured = cv2.GaussianBlur(gray,(21,21),0)
    if origImg is None:  ## I don't know why but I have to reload 1st image
                         ## to diffImg be correct
        _,img = cam.read()
        img = imutils.resize(img, width=500)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blured = cv2.GaussianBlur(gray,(21,21),0)
        origImg = blured
        continue
    diffImg = cv2.absdiff(origImg, blured)
    _, bw = cv2.threshold(diffImg,25,255,cv2.THRESH_BINARY)
    bw = cv2.dilate(bw, None, iterations=2)
    contours = cv2.findContours(bw.copy(),
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    cnt = 1
    for c in contours:
            if cv2.contourArea(c) < area:
                    continue
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, str(cnt), (x+w-15, y+15),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cnt+=1
    cv2.imshow("FaceDetection",img)
    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):   ## quit
        break
    if key==ord("r"):   ## reload first image again
                        ## new scene or stabilization
        origImg = None
cam.release()
cv2.destroyAllWindows()