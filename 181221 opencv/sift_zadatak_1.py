import numpy as np
import cv2


img1 = cv2.imread("car.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("prviframe.jpg", cv2.IMREAD_GRAYSCALE)

sift = cv2.SIFT_create()

#key points na prvoj slici
kp1 ,desc1 = sift.detectAndCompute(img1, None)
img1_keypoints = cv2.drawKeypoints(img1, kp1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imshow("keypoints1", img1_keypoints)
# cv2.waitKey()

#key points na drugoj slici
kp2 ,desc2 = sift.detectAndCompute(img2, None)
img2_keypoints = cv2.drawKeypoints(img2, kp2, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imshow("keypoints1", img2_keypoints)
# cv2.waitKey()


matcher = cv2.BFMatcher()
matches = matcher.knnMatch(desc1, desc2, k=2)
#img_matches = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append([m]) # m mora biti u uglatim zagradama da bi se mogao isprintati

img_matches = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good_matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)





cv2.imshow("img matches", img_matches)

cv2.waitKey()
cv2.destroyAllWindows()