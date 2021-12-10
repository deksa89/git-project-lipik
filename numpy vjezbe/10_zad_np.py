#     10.  Zadatak
# Stvorite 3D Numpy polje dimenzija 3x576x720. Stvorite novo Numpy polje koje sadrži iste elemente prvog polja,
#     ali u obliku 576x720x3. Koja Numpy funkcija je prigodna kako bi se ovo ostvarilo?
import numpy as np

a = np.full((3,576, 720),5)

b = a.swapaxes(1,2)
b = b.swapaxes(0,2)
print(b.shape)
