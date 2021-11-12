"""8 Unesi neki nasumični broj kojeg ćeš uzeti kao vrijednost duljine liste u koju se trebaju spremiti vrijednosti od 0 do 1001. 
	Ispiši sljedeće vrijednosti na ekran:
		a) medijan
		b) mod
		c) aritmetičku vrijednost
		d) sve brojeve koji se u definiranoj listi nalaze ispred vrijednosti koju smo izračunali kao medijan navedene liste
		e) sve brojeve koji su manji od vrijednosti koju smo izračunali kao medijan navedene liste 

	*Bonus: Napravite novu listu koja sadrži samo vrijednosti koje su za 10% veće ili manje od aritmetičke sredine"""

import random
import statistics

a = int(input("Unesi zeljenu duzinu liste: "))

lista = []
while len(lista) < a:
    x = random.randint(0,1001)
    lista.append(x)

print(f"Ovo je lista: {lista}")

#a)
median = statistics.median(lista)
print(f"Ovo je median: {median}")


#b)
from collections import Counter

def mod(lista):
    data = Counter(lista)
    return data.most_common(1)[0][0]

print(f"Ovo je mod liste: {mod(lista)}")

#c)
srednja_vrj = sum(lista) / len(lista)

print(f"Ovo je srednja vrijednost: {srednja_vrj}")

#d)
veci_brojevi = []
for i in lista:
    if i > median:
        veci_brojevi.append(i)

print(f"Ovo su brojevi veci od mediana: {veci_brojevi}")

#e)
manji_brojevi = []
for i in lista:
    if i < median:
        manji_brojevi.append(i)

print(f"Ovo su brojevi manji od mediana: {manji_brojevi}")


#bonus

veci_ili_manji = []

postotak = srednja_vrj * 0.1
for j in lista:
    if j < postotak + srednja_vrj and j > srednja_vrj-postotak:
        veci_ili_manji.append(j)

print(f"postotak {veci_ili_manji}")

