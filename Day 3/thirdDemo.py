import cv2

img = cv2.imread("Saved.png")
greyed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('greyed.png', greyed)
cv2.imshow("Original ",img)
cv2.imshow("Grayed ", greyed)
cv2.waitKey(0)

cv2.destroyAllWindows()
