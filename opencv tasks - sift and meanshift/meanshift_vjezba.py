import numpy as np
import cv2
import math

cap = cv2.VideoCapture("car_meanshift.mp4")
if not cap.isOpened():
    print("video not open")
    exit(1)

cv2.namedWindow('roi',cv2.WINDOW_NORMAL)

_, frame = cap.read()
#cv2.imwrite("crveniauto.jpg",frame)

x,y,w,h = 223, 202, 34, 20
track_window = (x,y,w,h)
roi = frame[y: y+h, x: x + w, :]
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
red_lower = np.array([170, 50, 50])
red_upper = np.array([180, 255, 255])
mask = cv2.inRange(roi_hsv, red_lower, red_upper)
roi_hist = cv2.calcHist([roi_hsv], [0], mask, [180], [0, 180])
roi_hist = cv2.normalize(roi_hist, None, 0, 255, cv2.NORM_MINMAX)


#cv2.imshow("roi", roi_hist)

fgbg = cv2.createBackgroundSubtractorMOG2()




#cv2.namedWindow('Input image',cv2.WINDOW_NORMAL)
#cv2.namedWindow('fgmask',cv2.WINDOW_NORMAL)
cv2.namedWindow('back proj img',cv2.WINDOW_NORMAL)


criteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv_frame], [0], roi_hist, [0,180], 1)

    _, track_window = cv2.meanShift(dst, track_window, criteria)
    x,y,w,h = track_window
    tracking_img = cv2.rectangle(frame, (x, y), (x + w, y + h), [255, 0, 0], 2)


    # fgmask = fgbg.apply(frame) nije potrebno za zadatak
    # kernel = np.ones((5, 5), np.uint8) nije potrebno za zadatak
    # bez_suma = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel) nije potrebno za zadatak


    # cv2.imshow('Input image', frame)
    # cv2.imshow('fgmask', fgmask)
    cv2.imshow("back proj img", tracking_img)

    key =  cv2.waitKey(24) & 0xFF
    if key == ord('q'):
        break

cv2.waitKey()
cap.release()
cv2.destroyAllWindows()