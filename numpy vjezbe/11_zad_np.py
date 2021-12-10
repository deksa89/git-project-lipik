#     11.  Zadatak
# Stvorite 2D Numpy polje dimenzija 2x3. Ukoliko je srednja vrijednost svih elemenata veća od 10 ispišite sumu svih elemenata,
#     u suprotnom ispišite vrijednost najvećeg elementa u polju.

import numpy as np

a = np.random.randint(1,10, size=(2, 3))
print(a)
print(a.max())
print(a.min())
print(a.prod())
a.sort()
print(a)
print(a.argmax())
print(a.argmin())