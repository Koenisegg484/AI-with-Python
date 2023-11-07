import cv2

img = cv2.imread("demo.jpg")
cv2.imshow("the demo image", img)

grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresholdImage = cv2.threshold(grayImage, 155, 220, cv2.THRESH_BINARY)[1]
cv2.imshow("threshold image", thresholdImage)

cv2.imwrite("thresholdimage.jpg", thresholdImage)

cv2.waitKey(0)
cv2.destroyAllWindows()