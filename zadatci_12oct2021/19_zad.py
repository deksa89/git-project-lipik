"""19. Omogućite unos dviju vrijednosti u dva navrata korisniku.
Svaki par vrijednosti zapišite u jedan tuple.
Zamijenite vrijednosti ovih dvaju tupleova te ispišite rezultat."""

a = tuple(input("Unesi prvi broj: "))
b = tuple(input("Unesi drugi broj: "))

a , b = b, a

print("".join(a))
print("".join(b))