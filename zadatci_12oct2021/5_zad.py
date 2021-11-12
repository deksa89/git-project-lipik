"""5. Omogućite unos 8 racionalnih brojeva te ispišite rezultat po sljedećoj formuli: 
a + b / c * d**e // f - g % h 
- komentarima ispišite što se sve događa kroz nekoliko slučajeva upisanih različitih brojeva"""


a =int(input("Unesi prvi broj: "))
b =int(input("Unesi drugi broj: "))
c =int(input("Unesi treci broj: "))
d =int(input("Unesi cetvrti broj: "))
e =int(input("Unesi peti broj: "))
f =int(input("Unesi sesti broj: "))
g =int(input("Unesi sedmi broj: "))
h =int(input("Unesi osmi broj: "))


x = a + b / c * d**e // f - g % h

#e je potencija na d, g % h dijeljenje koje vraca ostatak(7/2=1), // ne vraca ostatak prilikom dijeljenja

print(x)