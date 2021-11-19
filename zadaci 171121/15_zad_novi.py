#15. Napišite program koji ispisuje koliko ima prostih brojeva između
# dva proizvoljna broja (prost broj je broj koji je djeljiv samo sa 1 i sa samim sobom)

x = 5
y = 55

lista_prostih = []
for i in range(x, y+1):
    prost = True
    for j in range(2, i):
        if i % j == 0:
            prost = False
    if prost:
        lista_prostih.append(i)
print(lista_prostih)