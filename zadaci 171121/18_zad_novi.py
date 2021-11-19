#18. Ispišite sve parne brojeve između 1 i 1000 koju su istovremeno djeljivi i s 5 i s 13.

x = list(range(1, 1000))
lista = []
for i in x:
    if i % 2 == 0 and i % 5 == 0 and i % 13 == 0:
        lista.append(i)
print(lista)