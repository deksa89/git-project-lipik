#12. Napišite program koji s tipkovnice učitava proizvoljni niz znakova. Nad učitanim nizom znakova napravite analizu je li taj niz palindrom
#ili nije. Niz je palindrom ako se isto čita slijeva nadesno ili pak zdesna nalijevo.

x = input("Unesi niz znakova da vidis da li je palindrom: ")

if x == x[::-1]:
    print("Uneseni niz je palindrom")
else:
    print("Niz nije palindrom")