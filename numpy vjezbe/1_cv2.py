# 1. Zadatak
# Pomoću Houghove transformacije detektirajte i nacrtajte pravce na slici “kamera3.jpeg”. Među
# detektiranim pravcima moraju biti detektirane i linije voznih traka.
import cv2
import numpy as np

im = cv2.imread("kamera3.jpeg", cv2.IMREAD_GRAYSCALE)
mask = np.zeros_like(im)
height, width = im.shape
print("height is:", height)
print("width is:", width)

x1 = 0
y1 = height #500
x2 = width/2
y2 = 0
x3 = width
y3 = height


rectangle_points = np.array([[(x1, y1), (x2, y2), (x3, y3)]], dtype=np.int32)
mask = cv2.fillPoly(mask, rectangle_points, 255)
masked_image = cv2.bitwise_and(im, mask)

zamucena = cv2.GaussianBlur(masked_image, (5,5), 0)
canny = cv2.Canny(zamucena, 180, 250)

# sta = np.pi/180
# hugh = cv2.HoughLinesP(canny, 1, sta, 100)
# for i in hugh:
#     line = i[0]
#     pt1 = (line[0], line[1])
#     pt2 = (line[2], line[3])
#     line_color = [0, 255, 0]
#     cv2.line(im, pt1, pt2, line_color)



cv2.imshow("linija",masked_image)
cv2.waitKey()