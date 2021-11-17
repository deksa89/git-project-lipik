#5. Kreiraj listu koja se sastoji od stringova i brojeva, te odvoji brojeve i stringove u zasebne liste

lista = [2,"guska", 3,"patka", 4,"fazna", 5, 2,"jezero", 3, 3, "ribe" , 4]

stringovi = []
brojevi = []

for i in lista:
    if type(i) == str:
        stringovi.append(i)
    elif type(i) == int:
        brojevi.append(i)

print(stringovi)
print(brojevi)