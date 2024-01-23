import imutils
import cv2

guavaLower = (30, 71, 31)
guavaUpper = (47, 255, 230)

cam = cv2.VideoCapture(1)

while True:
    _,img = cam.read()
    img = imutils.resize(img, width=600)
    gauss = cv2.GaussianBlur(img, (11,11), 0)
    hsv = cv2.cvtColor(gauss, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, guavaLower, guavaUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius)= cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
        if radius > 10:
            cv2.circle(img, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(img, center, 5,  (0, 255, 255), -1)

            if radius > 250:
                print("STOP")
            else:
                if(center[0] < 150):
                    print("LEFT")
                elif(center[0] > 450):
                    print("RIGHT")
                elif(radius <    250):
                    print("FRONT")
                else:
                    print("STOP")

    cv2.imshow("Camera Feed", img)
    key = cv2.waitKey(1) & 0xFF
    if(key == ord("q")):
        break

cam.release()
cv2.destroyAllWindows()
