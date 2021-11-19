#14. Odaberite proizvoljno koordinatu T=(x,y), vrijednosti varijabli x (stupac) i y (redak) neka budu manje od 10. Program neka ispiše
#polje 10x10 čiji su svi elementi vrijednosti "-" osim koordinate T čija je vrijednost "X".

#Primjer: T=(1,1)
#- - - - - - - - - -
#- X - - - - - - - -
#- - - - - - - - - -
#- - - - - - - - - -
#- - - - - - - - - -
#- - - - - - - - - -
#- - - - - - - - - -
#- - - - - - - - - -
#- - - - - - - - - -
#- - - - - - - - - -


n = 10
x = 5
y = 5

def koordinatni_sustav(x,y):
    if x > 0 and y > 0: # <== moze i bez ovoga, samo mi ovo malo vise ima smisla :D
        for i in range(1, n+1):
            for j in range(1, n+1):
                if x == i and y == j:
                    print(" X ", end="")
                else:
                    print(" - ", end="")
            print()


print(koordinatni_sustav(x, y))