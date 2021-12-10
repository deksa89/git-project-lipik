#     6.  Zadatak
# Stvorite jediničnu matricu dimenzije 4x4, te još jednu matricu istih dimenzija čiji svi elementi imaju vrijednost 9. Ispišite na ekran:
#     • Zbroj
#     • Razliku
#     • Umnožak (element po element)
#     • Količnik

import numpy as np

a = np.eye(4)
#print(a)

b = np.full(4, 9)
#print(b)

suma = a + b
razlika = a - b
umnozak = a * b
kolicnik = a/b

print(suma)
print(razlika)
print(umnozak)
print(kolicnik)