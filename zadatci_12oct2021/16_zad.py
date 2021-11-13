"""16. Unesite dva proizvoljna niza znakova te ih spremite u dvije varijable. Prvi niz znakova mora imati više unesenih riječi od drugog niza znakova.
Od vrijednosti te dvije varijable napravite dvije liste te kreirajte konačni rječnik gdje će vrijednosti iz druge liste biti ključevi, 
a vrijednosti iz prve liste postati vrijednosti koje se pozivom ključa ispisuju."""

a = "ja sam pero peric"
b = "iz dakova grada"

a = list(a.split(" "))
b = list(b.split(" "))

x = dict(zip(b,a))
print(x) #nadam se da sam dobro shvatio zadatak