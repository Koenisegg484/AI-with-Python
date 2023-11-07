import cv2

img = cv2.imread("demo.jpg")

cv2.imshow("Me Myself", img)
cv2.imwrite("Saved.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
