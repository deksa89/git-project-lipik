# 1. Zadatak
# Using Hough's transformation, detect and draw directions in the image "kamera3.jpeg".
# Lines of lanes must be detected among the detected routes.

import cv2
import numpy as np

slika = cv2.imread("kamera3.jpeg")
im = cv2.imread("kamera3.jpeg", cv2.IMREAD_GRAYSCALE)

zamucena = cv2.GaussianBlur(slika, (5,5), 0)
canny = cv2.Canny(zamucena, 100, 150)

mask = np.zeros_like(canny)
height, width = canny.shape
print("height is:", height)
print("width is:", width)

x1 = 0
y1 = height
x2 = width*(2/4)
y2 = 150
x3 = width*(2/4)
y3 = 150
x4 = width
y4 = height

rectangle_points = np.array([[(x1, y1), (x2, y2), (x3, y3), (x4, y4)]], dtype=np.int32)
mask = cv2.fillPoly(mask, rectangle_points, 255)
masked_image = cv2.bitwise_and(canny, mask)

sta = np.pi/180
hugh = cv2.HoughLinesP(masked_image, 1, sta, 100)
for i in hugh:
    line = i[0]
    pt1 = (line[0], line[1])
    pt2 = (line[2], line[3])
    line_color = [0, 255, 0]
    cv2.line(slika, pt1, pt2, line_color)


cv2.imshow("maska", masked_image)
cv2.imshow("linija",slika)
cv2.waitKey()