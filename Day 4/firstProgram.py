import cv2
import imutils

img = cv2.imread("demo.jpg")
cv2.imshow("the demo image", img)

resizedImg = imutils.resize(img, width=1000)

cv2.imwrite("resised.jpg", resizedImg)
cv2.imshow("the resized image", resizedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()