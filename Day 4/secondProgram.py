import cv2

img = cv2.imread("demo.jpg")
cv2.imshow("the demo image", img)
gaussianBlurimg = cv2.GaussianBlur(img, (15, 15), 15)
cv2.imwrite("blurred.jpg", gaussianBlurimg)
cv2.imshow("blurred", gaussianBlurimg)

cv2.waitKey(0)
cv2.destroyAllWindows()
