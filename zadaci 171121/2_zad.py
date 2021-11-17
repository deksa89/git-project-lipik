#2. Napravi obrtaljku od unesenog stringa te na svakom drugom mjestu pridruzi nasumičan broj.

import random
x = "lipik"[::-1]
x = list(x)


i = 1
while i < len(x):
    x.insert(i, random.randint(0,10))
    i += 2

print(str(x))
    


