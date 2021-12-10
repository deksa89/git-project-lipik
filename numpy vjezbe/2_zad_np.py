#    2.  Zadatak
# Promijenite tip Numpy polja iz prethodnog zadatka u np.int16, te ispišite na ekran novi tip polja.

import numpy as np

a = np.ones((3,4,2))
a.dtype = np.int16
print(a.dtype)