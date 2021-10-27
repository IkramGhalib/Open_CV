import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required= True, help="Path to Input image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray)
cv2.imshow("blurred Image", blurred)

wide = cv2.Canny(blurred, 10, 250)
mid = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 240, 250)

cv2.imshow("wide Image", wide)
cv2.imshow("mid Image", mid)
cv2.imshow("tight Image", tight)
cv2.waitKey(0)
