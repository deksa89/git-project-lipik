lista = []

x = int(input("Unesi brojeve, za prekid stisni 0: "))
lista.append(x)
while x > 0:
    x = int(input("Unesi brojeve, za prekid stisni 0: "))
    lista.append(x)

bez_nule = lista[:-1]
sume = []
for i in bez_nule:
    i = str(i)
    suma = sum(int(x) for x in i if x.isdigit())
    sume.append(suma)

print(lista)
print(min(sume))