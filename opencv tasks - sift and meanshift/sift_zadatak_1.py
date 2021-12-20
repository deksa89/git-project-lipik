import numpy as np
import cv2
import time


video = cv2.VideoCapture("dashcam_video.mp4")
ret, frame = video.read()
# cv2.imwrite("drugiframe.jpg", frame)

x, y, w, h = 390, 300, 140, 120
track_window = (x, y, w, h)
roi = frame[y: y + h, x: x + w, :]
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
grey_lower = np.array([100, 20, 20])
grey_upper = np.array([130, 80, 200])
mask = cv2.inRange(roi_hsv, grey_lower, grey_upper)
roi_hist = cv2.calcHist([roi_hsv], [0], mask, [180], [0, 180])
roi_hist = cv2.normalize(roi_hist, None, 0, 255, cv2.NORM_MINMAX)

criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

# cv2.imshow("img matches", mask)
# cv2.waitKey()

cv2.namedWindow("img matches", cv2.WINDOW_NORMAL)
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)


try:
    fr = 0
    while True:
        fr += 1
        print(fr)
        ret, frame = video.read()
        if fr % 24 == 0:

            #creating a bounding box
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv_frame], [0], roi_hist, [0,180], 1)

            _, track_window = cv2.meanShift(dst, track_window, criteria)
            x, y, w, h = track_window

            tracking_img = cv2.rectangle(frame, (x, y), (x + w, y + h), [255, 0, 0], 2)

            #using sift function to recognize a car
            img1 = cv2.imread("car.png", cv2.IMREAD_GRAYSCALE)
            #img2 = cv2.imread("prviframe.jpg", cv2.IMREAD_GRAYSCALE)

            sift = cv2.SIFT_create()

            #key points na prvoj slici
            kp1 ,desc1 = sift.detectAndCompute(img1, None)
            img1_keypoints = cv2.drawKeypoints(img1, kp1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            # cv2.imshow("keypoints1", img1_keypoints)
            # cv2.waitKey()

            #key points na drugoj slici
            kp2 ,desc2 = sift.detectAndCompute(frame, None)
            img2_keypoints = cv2.drawKeypoints(frame, kp2, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            # cv2.imshow("keypoints1", img2_keypoints)
            # cv2.waitKey()

            matcher = cv2.BFMatcher()
            matches = matcher.knnMatch(desc1, desc2, k=2)
            #img_matches = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

            good_matches = []
            for m, n in matches:
                if m.distance < 0.7 * n.distance:
                    good_matches.append([m]) # m mora biti u uglatim zagradama da bi se mogao isprintati

            img_matches = cv2.drawMatchesKnn(img1, kp1, frame, kp2, good_matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

            cv2.imshow("img matches", img_matches)
            #cv2.imshow("frame", frame)
        else:
            cv2.imshow("frame", frame)


        key = cv2.waitKey(24) & 0xFF
        if key == ord('q'):
            break
except:
    print("video ends!")
    quit()


video.release()
cv2.waitKey()
cv2.destroyAllWindows()