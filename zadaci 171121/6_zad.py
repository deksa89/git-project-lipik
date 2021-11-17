"""6. S tipkovnice učitavajte cijele brojeve. Prvi upisani broj može biti bilo 
koji cijeli broj. Učitavanje ponavljati dok god je upisani broj strogo 
veći od prethodno upisanog broja. Ispisati sumu svih učitanih brojeva 
osim broja zbog kojeg je prekinuto učitavanje."""

suma = 0

x = int(input("unesi neki broj: "))

suma += x

while True:
    prethodni = x

    x = int(input("unesi neki broj: "))

    if x <= prethodni:
        break

    suma += x

print(suma)
