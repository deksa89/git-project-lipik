#     8.  Zadatak
# Stvorite 2D ndarray dimenzija 5x6 s elementima proizvoljnih vrijednosti.
#     Bez korištelja for petlje izdvojite svaki drugi stupac u zasebnu varijablu. Također, u zasebnu varijablu izdvojite posljednja 3 retka.
import numpy as np

a = np.random.randint(1, 9+1, size=(5,6))
print(a)

b = a[2:,:]
print(b)