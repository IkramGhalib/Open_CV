import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


recKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, recKernel)

tophat =cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, recKernel)


cv2.imshow("Original:", image)
cv2.imshow("Black Hat:", blackhat)
cv2.imshow("White Hat:", tophat)
cv2.waitKey(0)