#     9.  Zadatak
# Stvorite 2D Numpy polje dimenzija 16x16 proizvoljnih vrijednosti. Stvorite novo Numpy polje koje sadrži iste elemente prvog polja, ali u obliku 4x8x8.
# Koja Numpy funkcija je prigodna kako bi se ovo ostvarilo? Vizualizirajte oblik novog ndarray-a. Dovoljna je skica na papiru ili skica u nekom digitalnom alatu.


import numpy as np

a = np.random.randint(1, 9+1, size=(16,16))
#print(a)

b = a.reshape((4,8,8))
print(b)