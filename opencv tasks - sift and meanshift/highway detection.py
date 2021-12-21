import numpy as np
import cv2

cap = cv2.VideoCapture("highway camera.mp4")

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=150)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("height is: ", height)
print("width is: ", width)
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()

    height, width, _ = frame.shape
    roi = frame[380:720, 100:1000]


    mask = object_detector.apply(roi)

    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    gaussian_blur = cv2.GaussianBlur(mask, (17, 17), 0)

    contours, _ = cv2.findContours(gaussian_blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 2000:
            #cv2.drawContours(roi, [cnt], -1, (0,255,0), 1)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x,y), (x + w, y + h), (0, 255, 0), 2)
            print([x,y,w,h])




    cv2.imshow("frame", frame)

    key = cv2.waitKey(20) & 0xFF
    if key == ord('q'):
        break


cap.release()
cv2.waitKey()
cv2.destroyAllWindows()