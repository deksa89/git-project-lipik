"""24. Automat s čokoladicama prima bilo koji iznos u kunama i vraća kovanice u sljedećim oblicima:
	1 lipa, 2 lipe, 5 lipa, 10 lipa, 20 lipa, 50 lipa, 1 kuna, 2 kune, 5 kuna
Potrebno je napisati funkciju koju će koristiti navedeni automat s čokoladicama kako bi vratio ostatak novca korisniku. 
Pretpostavka je da automat uvijek vraća najmanji mogući broj kovanica.
Funkcija prima 2 parametra - količinu novca kojeg je korisnik ubacio i cijenu proizvoda
Funkcija vraća listu brojeva. Svaki od tih brojeva predstavlja količinu jedne vrste kovanice."""

ubaceno = 20
cijena = 7.99

def automat(ubaceno, cijena):
    ostatak = ubaceno - cijena

    kn_5 = 0
    kn_2 = 0
    kn_1 = 0
    kn_050 = 0
    kn_020 = 0
    kn_010 = 0
    kn_005 = 0
    kn_002 = 0
    kn_001 = 0


    while ostatak >= 5:
        ostatak -= 5
        kn_5 += 1
    while ostatak >= 2:
        ostatak -= 2
        kn_2 += 1
    while ostatak >= 1:
        ostatak -= 1
        kn_1 += 1
    while ostatak >= 0.50:
        ostatak -= 0.50
        kn_050 += 1
    while ostatak >= 0.20:
        ostatak -= 0.20
        kn_020 += 1
    while ostatak >= 0.10:
        ostatak -= 0.10
        kn_010 += 1
    while ostatak >= 0.05:
        ostatak -= 0.05
        kn_005 += 1
    while ostatak >= 0.02:
        ostatak -= 0.02
        kn_002 += 1
    while ostatak >= 0.005:
        ostatak -= 0.005
        kn_001 += 1

    return f"Automat je vratio kovanicu od 5 kn {kn_5} puta, od 2 kn {kn_2} puta, od 1 kn {kn_1} puta, od 50 lipa {kn_050} puta, \n " \
           f" od 20 lipa {kn_020} puta, od 10 lipa {kn_010} puta, od 5 lipa {kn_005} puta, od 2 lipa {kn_002} puta, od 1 lipa {kn_001} puta."

print(automat(ubaceno,cijena))