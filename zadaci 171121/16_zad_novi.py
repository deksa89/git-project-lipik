#16. Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni niz znakova i brojčanu varijablu n. Provjerite je li vrijednost varijable
#n manja od broja znakova u nizu. Ako je vrijednost varijable n veća ispišite informaciju o grešci. Ispišite iz niza znakova svako n-to
#slovo. Na primjer, ulazni niz je "ABCDEFGH", n je 2, tada je izlaz "ACEG".

n = 3
x = "ABCDEFGH"

def fun(x, n):
    lista = []
    if len(x) < n:
        print("greska")
    else:
        for i, j in enumerate(x):
            if i % n == 0:
                lista.append(j)
    return lista

print(fun(x, n))