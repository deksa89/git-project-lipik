#3.  Napiši program koji upisuje bodove n plesnih natjecanja. Ispiši zbroj svih bodova tako da odbaciš najbolji i najlošiji rezultat.


def natjecanje():
    lista_bodova = []
    
    while len(lista_bodova) < 10:
        bodovi = int(input("Unesi bodove: "))
        lista_bodova.append(bodovi)
    
    lista_bodova.remove(max(lista_bodova))
    lista_bodova.remove(min(lista_bodova))
    suma = sum(lista_bodova)
    return suma, lista_bodova
    

print(natjecanje())