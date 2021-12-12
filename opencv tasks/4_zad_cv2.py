# 4. Zadatak
# Pomoću Houghove transformacije pokušajte detektirati prometni znak i linije ruba ceste na slici “kamera4.png”.
import cv2
import numpy as np

#importing the image
image_road = cv2.imread("kamera4.png")

#switching the image to black and white
black_white = cv2.imread("kamera4.png", cv2.IMREAD_GRAYSCALE)

#trying to compare both methods of bluring images
# median_blur = cv2.medianBlur(black_white, 15)
# canny = cv2.Canny(median_blur, 80, 120)

#applying gaussian blur in order to blur potential pixels that could enter an image in which we will detect straight lines
gaussian_blur = cv2.GaussianBlur(black_white, (17,17), 0)
canny2 = cv2.Canny(gaussian_blur, 60, 70)

#making a mask that will mask unecessary part of the image in order to speed up a process of image processing
cutted_out = np.zeros_like(canny2)
height, width = canny2.shape
#print("visina je:", height)
#print("širina je:", width)

x1 = width / 2
y1 = height
x2 = width / 2
y2 = 0
x3 = width
y3 = 0
x4 = width
y4 = height

rectangle_points = np.array([[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]], dtype=np.int32)
mask = cv2.fillPoly(cutted_out, rectangle_points, 255)
masked_img = cv2.bitwise_and(canny2, mask)

try:
    #finding boundary line on cropped image through a for loop
    theta = np.pi/180
    hugh_lines = cv2.HoughLinesP(masked_img, 1, theta, 100)
    for i in hugh_lines:
        line = i[0]
        pt1 = (line[0], line[1])
        pt2 = (line[2], line[3])
        cv2.line(image_road, pt1, pt2,(206, 245, 66), 2)


    #circle detection
    rows = black_white.shape[0]
    hugh_circles = cv2.HoughCircles(masked_img, cv2.HOUGH_GRADIENT, 1, rows/8, param1=100, param2=30,
                                   minRadius=10, maxRadius=50)

    circles = np.uint16(np.around(hugh_circles))
    for i in circles[0, :]:
        print(i)
        center = (i[0], i[1])
        # circle center
        cv2.circle(image_road, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv2.circle(image_road, center, radius, (245, 227, 66), 2)

except:
    print("ne nalazi linije ili krugove")


cv2.imshow("linije", image_road)
cv2.waitKey()
cv2.destroyAllWindows()