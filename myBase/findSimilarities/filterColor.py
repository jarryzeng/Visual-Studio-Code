import cv2
import numpy as np

def empty(value):
    pass

local = "findSimilarities/"
img = cv2.imread(f"{local}img.jpg")

cv2.namedWindow("contral filter")
cv2.resizeWindow("contral filter", 640, 320)
cv2.createTrackbar("Hue Min", "contral filter", 0, 179, empty)
cv2.createTrackbar("Hue Max", "contral filter", 179, 179, empty)
cv2.createTrackbar("Sat Min", "contral filter", 0, 255, empty)
cv2.createTrackbar("Sat Max", "contral filter", 255, 255, empty)
cv2.createTrackbar("Val Min", "contral filter", 0, 255, empty)
cv2.createTrackbar("Val Max", "contral filter", 255, 255, empty)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
while True:
    hmin = cv2.getTrackbarPos("Hue Min", "contral filter")
    hmax = cv2.getTrackbarPos("Hue Min", "contral filter")
    smin = cv2.getTrackbarPos("Sat Min", "contral filter")
    smax = cv2.getTrackbarPos("Sat Max", "contral filter")
    vmin = cv2.getTrackbarPos("Val Min", "contral filter")
    vmax = cv2.getTrackbarPos("Val Max", "contral filter")
    
    lower = np.array([hmin, smin, vmin])
    upper = np.array([hmax, smax, vmax])
    
    mask = cv2.inRange(hsv, lower, upper)
    
    cv2.imshow("img", img)
    cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.waitKey(1)