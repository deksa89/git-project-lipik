"""20. Omogućite korisniku unos dviju vrijednosti n puta korisniku. 
Sortirajte sve unose koristeći druge vrijednosti iz svakog unosa."""

a = int(input("Unesi prvi broj: "))
b = int(input("Unesi drugi broj: "))
c = int(input("Koliko puta zelis ponoviti unesena dva broja: "))


def broj_ponavljanja(a,b,c):
    lista = []
    while len(lista) < c:
        lista.append(a)
        lista.append(b)
    return sorted(lista)

print(broj_ponavljanja(a,b,c)) #ne razumijem zadatak, nadam se da je ovo donekle slicno onom sto ste zamislili 