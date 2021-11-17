"""8. Napišite program koji s tipkovnice učitava proizvoljni cijeli 
troznamenkasti broj. Ako učitani broj nije troznamenkasti, ispišite 
poruku o greški i prekinite daljnje izvođenje programa. U slučaju da 
je učitani broj ispravan, ispišite prvi sljedeći troznamenkasti 
palindrom. Na primjer, ako je učitani broj 120, prvi sljedeći palindrom 
je 121."""

x = int(input("unesi troznamenkasti broj: "))
def palindrom(x):
    if x < 100 or x > 999:
        quit("broj nije troznamenkast")
    
    return str(x) == str(x)[::-1]


if str(x) == str(x)[::-1]:
        print(f"{x} je palindrome") 

else:
    y = x
    while not palindrom(y):
        y = int(y)+1
    print(f"slijedeci palindrom je {y}") 

