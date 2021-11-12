"""11. U varijablu upišite neki proizvoljni niz znakova. Nad varijablom pozovite odgovarajuću funkciju koja će vratiti duljinu upisanoga niza znakova te rezultat spremite u novu varijablu. 
Ispišite sve znakove do polovice niza. 
Primjer: ako imamo niz od 15 znakova (abcdefghijklmno), potrebno je ispisati 1., 2., 3., 4., 5., 6., 7. i 8. znak (abcdefgh)"""

import math
string = "abcdefgh"

if len(string) % 2 != 0:
    a = math.floor(len(string)/2)
    print(string[:a])
else:
    b = int(len(string)/2)
    print(string[:b])

