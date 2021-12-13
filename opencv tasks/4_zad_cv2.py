# 4. Task
# Using Hough's transformation, try to detect a traffic sign and road edge lines in the image "kamera4.png".

import cv2
import numpy as np

#importing the image
image_road = cv2.imread("kamera4.png")
cv2.imshow("linija", image_road)
#switching the image to black and white
black_white = cv2.imread("kamera4.png", cv2.IMREAD_GRAYSCALE)

#trying to compare both methods of bluring images
# median_blur = cv2.medianBlur(black_white, 15)
# canny = cv2.Canny(median_blur, 80, 120)

#trying which filter suits better here
#deciding to apply gaussian blur in order to blur potential pixels that could enter an image in which we will detect straight lines
gaussian_blur = cv2.GaussianBlur(black_white, (21,21), 0)

#bilateral = cv2.bilateralFilter(gaussian_blur,10, 25, 10)

canny2 = cv2.Canny(gaussian_blur, 40, 50)


try:
    # making a mask that will mask unecessary part of the image in order to speed up a process of image processing
    cutted_out_lanes = np.zeros_like(canny2)
    height, width = canny2.shape
    # print("visina je:", height)
    # print("širina je:", width)

    x1 = 0
    y1 = height
    x2 = width * (2/5)
    y2 = height / 2
    x3 = width * (4/5)
    y3 = height / 2
    x4 = width
    y4 = height


    #road lanes mask
    rectangle_points = np.array([[(x1, y1), (x2, y2), (x3, y3), (x4, y4)]], dtype=np.int32)
    mask = cv2.fillPoly(cutted_out_lanes, rectangle_points, 255)
    masked_img = cv2.bitwise_and(canny2, mask)

    #finding road lines on cropped image through a for loop
    minLineLength = 100
    hugh_lines = cv2.HoughLinesP(masked_img, rho=1, theta=np.pi/180, threshold=70, lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)
    for i in hugh_lines:
        line = i[0]
        pt1 = (line[0], line[1])
        pt2 = (line[2], line[3])
        cv2.line(image_road, pt1, pt2,(206, 245, 66), 2)


    #######################################
    #######################################

    # making a mask that will mask unecessary part of the image in order to speed up a process of image processing
    cutted_out_circle = np.zeros_like(canny2)
    height, width = canny2.shape
    # print("visina je:", height)
    # print("širina je:", width)

    x1 = width / 2
    y1 = height
    x2 = width / 2
    y2 = 0
    x3 = width
    y3 = 0
    x4 = width
    y4 = height

    #circle mask
    rectangle_points = np.array([[(x1, y1), (x2, y2), (x3, y3), (x4, y4)]], dtype=np.int32)
    mask1 = cv2.fillPoly(cutted_out_circle, rectangle_points, 255)
    masked_img1 = cv2.bitwise_and(canny2, mask1)

    #circle detection
    rows = black_white.shape[0]
    hugh_circles = cv2.HoughCircles(masked_img1, cv2.HOUGH_GRADIENT, 1, rows/8, param1=100, param2=30,
                                   minRadius=10, maxRadius=50)

    circles = np.uint16(np.around(hugh_circles))
    for i in circles[0, :]:
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