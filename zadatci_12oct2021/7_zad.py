#7. Ispiši vrijednost broja Pi na 4 decimalna mjesta, kvadriraj taj broj te ga podijeli s racionalnim brojem odabranim od strane korisnika (input funkcija) i ispiši rezultat.

import math
a =int(input("Unesi neki broj: "))

y = round((math.pi),4)
x = (y**2)/a

print(x)