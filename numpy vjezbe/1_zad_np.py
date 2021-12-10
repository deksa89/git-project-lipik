#    1.  Zadatak
# Stvorite Numpy array objekt iz Python 3D matrice veličine 3x4x2. Tip elemenata Numpy polja mora biti numpy.float64.
# Ispišite na ekran:
#     • Broj osi
#     • Dimenzije polja
#     • Ukupni broj elemenata u polju
#     • Tip elemenata u polju
import numpy as np

a = np.ones((3,4,2))

print(a.ndim) #broj osi
print(a.shape) #dimenzije polja
print(a.size) #ukupni broj elemenata u polju
print(a.dtype) #tip elemenata u polju



