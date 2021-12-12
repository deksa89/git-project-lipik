# 3. Zadatak
# Pomoću Houghove transformacije detektirajte i nacrtajte pravce na slici “puna_linija_desno.jpg”.
# Među detektiranim pravcima mora biti samo desna puna linija.
# Izmijenite kôd tako da se među detektiranim linijama također nalaze i isprekidane linije
# autoceste.

import cv2
import numpy as np

slika = cv2.imread("puna_linija_desno.jpg")
crno_bijela = cv2.imread("puna_linija_desno.jpg", cv2.IMREAD_GRAYSCALE)

gausian_blur = cv2.GaussianBlur(crno_bijela, (13,13), 0)
canny = cv2.Canny(gausian_blur, 50, 60)

maska = np.zeros_like(canny)
height, width = canny.shape
print("visina je:", height)
print("širina je:", width)

x1 = 0
y1 = height
x2 = 0
y2 = height * (3/5)
x3 = width * (3/5)
y3 = height * (3/5)
x4 = width
y4 = height


rectangle_points = np.array([[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]], dtype=np.int32)
mask = cv2.fillPoly(maska, rectangle_points, 255)
maskirana_slika = cv2.bitwise_and(canny, mask)

theta = np.pi/180
hugh_lines = cv2.HoughLinesP(maskirana_slika, 80, theta, 100)
for i in hugh_lines:
    line = i[0]
    pt1 = (line[0], line[1])
    pt2 = (line[2], line[3])
    cv2.line(slika, pt1, pt2,(206, 245, 66), 2)  #(image, start_point, end_point, color, thickness)


# cv2.imshow("mas", maskirana_slika)
cv2.imshow("cb", slika)
cv2.waitKey()
cv2.destroyAllWindows()