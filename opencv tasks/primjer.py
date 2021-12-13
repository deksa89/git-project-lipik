import cv2
import numpy as np

# kamion = cv2.imread("C:/Users/deksa/Desktop/Predavanja feritovci/Zadaci/playing with opencv/kamion.jpg")
# print(type(kamion))
# cv2.imshow("kamion.jpg", kamion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(kamion.shape)


# B, G, R = kamion[10, 50]
# print(B, G, R)
# print(kamion.shape)

# siva = cv2.cvtColor(kamion, cv2.COLOR_BGR2GRAY)
# cv2.imshow("siva", siva)
# cv2.waitKey(0)


# hsv_slika = cv2.cvtColor(kamion, cv2.COLOR_BGR2HSV)
#
# cv2.imshow("hsv slika", hsv_slika[:,:,2])
# cv2.waitKey(0)


# a = np.random.randint(1,9, size=(4,4))
# print(a)
#
# b = a[2:, 2:]
# print(b)

# a = np.array([1,2,3,4,5,6,7,8,9,10])
# a[1::2] = 99
# print(a)

# a = np.identity(4, dtype=int)
# print(a)

# b = np.eye(4,2, dtype=int)
# print(b)

# b = np.full(4, 9)
# print(b)
#
# suma = a + b
# umnozak = a*b
# print(suma)
# print(umnozak)

# a = np.linspace(2,21, 12)
# print(a)


kamera = cv2.imread("kamera1.jpg")
# cv2.imshow("kamera", kamera)
# cv2.waitKey()

# B, G, R = cv2.split(kamera)
# #print(B.shape)
#
# merged = cv2.merge([R, G+200, B])

# B, G, R = cv2.split(kamera)
# zeros = np.zeros(kamera.shape[:2], dtype="uint8")

# kernel = np.ones((7,7), np.float32) / 49
# blurred = cv2.filter2D(kamera, -1, kernel)

blur = cv2.GaussianBlur(kamera,(7,7), 0)


cv2.imshow("R",blur)
cv2.waitKey()










