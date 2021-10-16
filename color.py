import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="Path to input image")

args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("R", image)
cv2.waitKey(0)

for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
    cv2.imshow(name, chan)
    cv2.waitKey(0)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV:", hsv)

for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
    cv2.imshow(name, chan)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
cv2.imshow("L*, a*, b*", lab)

for (name, chan) in zip(("l*","a*", "b*"), cv2.split(lab)):
    cv2.imshow(name, chan)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
