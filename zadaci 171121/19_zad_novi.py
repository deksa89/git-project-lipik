#19. Napisi program koji unosi n brojeva i od znamenke desetice svakog broja stvara novi broj.

import random

lista = []
while len(lista) < 10:
    x = random.randint(10, 99)
    lista.append(x)

print(lista)

lista_str = str(lista)
lista_str = lista_str.split(",")

lista_desetice = []
for i in lista_str:
    desetica = i[1]
    lista_desetice.append(desetica)

print(list(lista_desetice))