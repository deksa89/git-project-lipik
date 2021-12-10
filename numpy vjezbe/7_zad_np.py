#     7.  Zadatak
# Stvorite 1D ndarray od 10 elemenata proizvoljnih vrijednosti. Bez korištenja for petlje postavite svaki drugi element u rasponu indeksa [2, 7> na vrijednost 99.
import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
a[::2] = 99
print(a)