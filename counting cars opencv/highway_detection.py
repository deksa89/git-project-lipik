import numpy as np
import cv2
from time import sleep


cap = cv2.VideoCapture("video.mp4")

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=150)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("height is: ", height)
print("width is: ", width)
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)

offset = 6
delay = 60
line_pos = 650

detec = []
cars = 0

def catch_center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy


while True:
    ret, frame = cap.read()

    height, width, _ = frame.shape
    roi = frame[480:720, 0:580]

    mask = object_detector.apply(roi)

    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    gaussian_blur = cv2.GaussianBlur(mask, (17, 17), 0)

    contours, h=cv2.findContours(gaussian_blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame, (25, line_pos), (1200, line_pos), (255, 127, 0), 3)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 2400:
            x, y, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(roi, (x,y), (x + w, y + h), (0, 255, 0), 2)
            centro = catch_center(x, y, w, h)
            detec.append(centro)
            cv2.circle(roi, centro, 4, (0, 0, 255), -1)

            for (x, y) in detec:
                print(y)
                if y >= 200 and y <= 210:
                    cars += 1
                    cv2.line(roi, (25, line_pos), (1200, line_pos), (0, 127, 255), 3)
                    detec.remove((x, y))
                print("car is detected : " + str(cars))

    cv2.putText(frame, "VEHICLE COUNT : " + str(cars), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    cv2.imshow("frame", frame)


    key = cv2.waitKey(90) & 0xFF
    if key == ord('q'):
        break


cap.release()
cv2.waitKey()
cv2.destroyAllWindows()