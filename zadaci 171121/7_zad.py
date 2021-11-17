"""7. Učitajte s tipkovnice 2 niza znakova, svaki od tih nizova znakova 
spremite u zasebnu varijablu. Ispišite indekse na kojima se pojavljuju 
ista slova neovisno o veličini ('a' i 'A' tretirati jednako)."""


"""a = input("unesi prvu rijec: ").lower()
b = input("unesi drugu rijec: ").lower()"""

b = "dean"
a = "jelena"

lista = []
for i, j in enumerate(a):
    for g, h in enumerate(b):
        if j == h:
            lista.append(i)
            lista.append(j)
    

print(lista)
    