"""14. Kreirajte varijablu te u nju spremite nasumični niz znakova. 
Na ekran s jednom print naredbom ispišite sljedeće: 
a) “prva riječ u nizu ima sva velika slova bez obzira na uneseni niz: <RIJEČ>” 
b) “druga riječ u nizu ima <XY> znakova”
c) “ne postoje bjeline iza unesenog niza znakova: <niz znakova>” 
d) “ne postoje bjeline prije unesenog niza znakova: <niz znakova>” 
e) “svi znakovi su ispisani malim slovom: <niz znakova>”, 
f) “samo prvo slovo cijelog niza je ispisano velikim slovom te je iza unesenog niza dodan niz “ asdfčlkasdfčlk” odmah nakon zadnjeg alfanumeričkog znaka: <niz znakova + ostatak>”"""


string = "inace sve pet"

#a)
a = string.split(" ")
prva = a[0].upper()
print(f"prva riječ u nizu ima sva velika slova bez obzira na uneseni niz: {prva}")

#b)
druga = len(a[1])
print(f"druga riječ u nizu ima {druga} znakova")

#c)
if string.isspace():
# rješenje: "inace sve pet"


#d)

#e)

#f)


