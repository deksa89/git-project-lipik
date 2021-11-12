"""6. Unesi jedan nasumični broj. 
Ispiši aritmetičku sredinu onoliko brojeva(0-101) koliko je iznosio uneseni nasumični broj.
Navedeni broj uzmi kao vrijednost opsega kruga te ispiši vrijednost polumjera navedenog kruga."""

import math
a =input("Unesi neki broj: ")

broj = 0
for i in a:
    broj += int(i)

y = broj / len(a)

radius = (y / math.pi) / 2

print(radius)