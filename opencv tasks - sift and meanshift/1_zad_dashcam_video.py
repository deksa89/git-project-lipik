import numpy as np
import cv2
import math

cap = cv2.VideoCapture("dashcam_video.mp4")

_, frame = cap.read()
x,y,h,w = 390, 300, 120, 140
track_window = (x,y,h,w)
roi_frame = frame[y: y+h, x: x+w, :]
roi_hsv = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2HSV)
red_lower = np.array([100, 20, 20])
red_upper = np.array([130, 80, 200])
mask = cv2.inRange(roi_hsv, red_lower, red_upper)
roi_hist = cv2.calcHist([roi_hsv], [0], mask, [180], [0, 180])
roi_hist = cv2.normalize(roi_hist, None, 0, 255, cv2.NORM_MINMAX)

criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)

cv2.imshow("img matches", roi_hsv)
cv2.waitKey()

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv_frame], [0], roi_hist, [0,180], 1)

    _, track_window = cv2.meanShift(dst, track_window, criteria)
    x,y,w,h = track_window
    tracking_img = cv2.rectangle(frame, (x, y), (x + w, y + h), [255, 0, 0], 2)

    cv2.imshow('Input image', tracking_img)


    key =  cv2.waitKey(25) & 0xFF
    if key == ord('q'):
        break




#cv2.imwrite("prviframe.jpg", frame) #za kreiranje jpg slike prvog framea
# cv2.imshow("frame", mask)
cv2.waitKey()
cap.release()
cv2.destroyAllWindows()

