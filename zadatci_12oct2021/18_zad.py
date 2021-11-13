"""18. Dobivate tuple sljedeće strukture: t = ("Jaje", [10, 20, 30], (5, 50, 500))
Napišite funkciju koja će printati vrijednost 20 iz tog tuplea. """

t = ("Jaje", [10, 20, 30], (5, 50, 500))

"""for i in t:
    for j in i:
        if j == 20:
            print(j)"""

#ili ovako:

t = t[1][1]
print(t)