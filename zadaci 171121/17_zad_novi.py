#17. Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni niz znakova. Ispišite koliko velikih slova se nalazi u nizu. Ako je neko od
#unesenih slova u nizu "A", brojanje velikih slova je potrebno prekinuti i ispisati informaciju da je veliko slovo "A" pronađeno.

x = "Jabuka, Kruska, Sljiva, Ananas, Kivi"

velika_slova = 0
for i in x:
    if i.isupper():
        velika_slova += 1
    if i == "A":
        print("veliko slovo A je pronadeno")
        break
print(velika_slova)