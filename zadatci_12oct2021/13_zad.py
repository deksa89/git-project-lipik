"""13. Spremite sljedeći niz znakova u varijablu: "Testiramo što sve možemo napraviti sa stringovima". Iz niza znakova u prethodnom zadatku dohvatite i ispišite: 
a) cijeli niz
b) riječ "string", 
c) koji je to tip podatka,
d) koje je početno slovo te riječi koristeći indekse
e) koje je posljednje slovo te riječi koristeći metode za stringove
f) koliko znakova ta riječ ima """

string = "Testiramo što sve možemo napraviti sa stringovima"

#a)
print(string)

#b)
print(string[38:-5])

#c)
print(type(string))

#d)
print(string[0])

#e)
print(string[-1])

#f)
print(len(string))