import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required = True, help= "Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.imshow("Original Image", image)
# cv2.waitKey(0)
#
# for i in range(0, 3):
#     eroded =cv2.erode(gray.copy(), None, iterations= i+1)
#     cv2.imshow("Eroded {}".format(i + 1), eroded)
#     cv2.waitKey(0)
#
# for i in range(0, 3):
#     dialation = cv2.dilate(gray.copy(), None, iterations= i+1)
#     cv2.imshow("Dialated {}".format(i+1), dialation)
#     cv2.waitKey(0)
#
# cv2.destroyAllWindows()
cv2.imshow("Original image", image)
cv2.waitKey(0)

kernelSizes = [(3, 3), (5, 5), (7, 7), (10, 10)]

# for kernelSize in kernelSizes:
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
#     opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
#     cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSizes[1]), opening)
#     cv2.waitKey(0)
#
# for kernelSize in kernelSizes:
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
#     closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
#     cv2.imshow("Closing: ({}, {})".format(kernelSize[0], kernelSizes[1]), closing)
#     cv2.waitKey(0)

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({},{})".format(kernelSize[0], kernelSize[1]),gradient)
    cv2.waitKey(0)

