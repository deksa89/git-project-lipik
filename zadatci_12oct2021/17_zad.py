"""17. Unesite tri proizvoljna niza znakova te ih spremite u tri varijable. 
Ispišite na ekran znakove (characters) koji su zajednički svim unesenim vrijednostima"""


a = "slavonija"
b = "hrvatska"
c = "europa"

x = ''.join(set(a).intersection(b))
y = ''.join(set(x).intersection(c))

print(y)