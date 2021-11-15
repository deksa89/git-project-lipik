"""23. Napiši funkciju koja će za neki input broj vratiti nested listu s dužinama sub-lista koje se povećavaju za 1.
	Rezultat bi trebao izgledati ovako: 
		pyramid(0) => [ ]
		pyramid(1) => [ [1] ]
		pyramid(2) => [ [1], [1, 1] ]
		pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
		pyramid(4) => ..."""

"""23. Napiši funkciju koja će za neki input broj vratiti nested listu s dužinama sub-lista koje se povećavaju za 1.
	Rezultat bi trebao izgledati ovako: 
		pyramid(0) => [ ]
		pyramid(1) => [ [1] ]
		pyramid(2) => [ [1], [1, 1] ]
		pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
		pyramid(4) => ..."""


x = int(input("Unesi neki broj: "))
list1 = []
red = 0

while red < x:
    jedan = red + 1
    sublist = []
    while jedan > 0:
        sublist.append(1)
        jedan -= 1

    list1.append(sublist)
    red += 1
    print(list1)