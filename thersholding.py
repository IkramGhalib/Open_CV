# python thersholding.py --image
# import the necessary packages
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="path to input image")
args = vars(ap.parse_args())

image =cv2.imread(args["image"])
cv2.imshow("Original:", image)
cv2.waitKey(0)



gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

(T, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh Binary inverse:", threshInv)

cv2.waitKey(0)

(T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold binary:", thresh)
cv2.waitKey(0)

mask = cv2.bitwise_and(image, image, mask=thresh)
cv2.imshow("Masked Image:", mask)
cv2.waitKey(0)