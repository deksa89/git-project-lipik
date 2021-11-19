#20. Napisi program koji unosi n brojeva i sastavlja novi broj od najvece znamenke u svakom od brojeva

x = [21,34,54,77,94,74,89,63,61]
x = str(x)
x = x.split(",")

nova = []
suma_nova = 0
for i in x:
    if i[1] > i[2]:
        nova.append(i[1])
        suma_nova += int(i[1])
    else:
        nova.append(i[2])
        suma_nova += int(i[2])

print(nova)
print(suma_nova)