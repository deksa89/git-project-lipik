#11. Napišite program koji s tipkovnice učitava cijeli broj n iz intervala [3, 20]. U slučaju da je unesena vrijednost neispravna, ispisati prikladnu
#poruku na ekran te zatražiti ponovni unos cijelog broja. Nakon učitane vrijednosti n, učitajte n parova cijelih brojeva. Nakon što je n
#parova brojeva učitano, ispišite parove brojeva koji imaju najveću sumu.


lista = []

x = int(input("Unesi broj izmedu 3 i 20: "))
if x not in range(3, 21):
    print("broj mora biti izmedu 3 i 20.")
elif x == 0:
    print(lista)
else:
    lista.append(x)
while x > 0:
    x = int(input("Unesi broj izmedu 3 i 20: "))
    if x in range(3, 21):
        lista.append(x)
    elif x not in range(3, 21):
        print("broj mora biti izmedu 3 i 20.")

sume = []
for i in lista:
    i = str(i)
    suma = sum(int(x) for x in i if x.isdigit())
    sume.append(suma)

print(sume)
print(min(sume))