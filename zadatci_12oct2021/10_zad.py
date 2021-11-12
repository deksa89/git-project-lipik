"""10. Napišite algoritam koji uzima broj nasumične dužine te ispisuje:
a) svaku drugu znamenku s tri decimalna mjesta (0,000) 
b) zaokružen zbroj svih upravo ispisanih znamenki"""

#a)
from typing import Sized


a = 12345678
a = str(a)

lista = []
suma = 0

for i in range(len(a)):
    if (i%2) != 0:
        lista.append(str(i)+".000")
        suma += i

print(lista)

#b)

print(suma)
