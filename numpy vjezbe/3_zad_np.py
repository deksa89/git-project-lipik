#     3.  Zadatak
# Stvorite 2x7x3 Numpy polje tipa numpy.int32 čiji svi elementi imaju vrijednost 9.
import numpy as np

a = np.full((2,7,3), 9)
print(a)
print(a.shape)