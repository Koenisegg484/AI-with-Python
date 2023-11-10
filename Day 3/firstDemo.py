import cv2
# img = cv2.imread("./jkl.png")
img = cv2.imread(r"C:\Users\shiva\OneDrive\Desktop\AI Pantech\Day 3\jkl.png")

if img is None:
    print("Error: Could not read the image. Please check the file path.")
else:
    cv2.imshow("Latom", img)
    cv2.imwrite("saved01.png", img)
    cv2.waitKey(0)
    print("waiting")
    cv2.destroyAllWindows()
    print("exitted")
