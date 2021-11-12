"4. Napišite program koji će u varijable a i b spremiti dva dvoznamenkasta broja." 
"U varijablu a pohranite zadnju znamenku broja koji se nalazi u varijabli b, a u varijablu b pohranite zadnju znamenku broja koja se nalazi u varijabli a. Ispišite sadržaj varijabli a i b."

a = input("Unesi prvi dvoznamenkasti broj: ")

if len(a) < 2 or len(a) > 2: 
    print ("moras unjeti dvoznamenkasti broj")
    quit()

b = input("Unesi drugi dvoznamenkasti broj: ")

if len(b) < 2 or len(b) > 2: 
    print ("moras unjeti dvoznamenkasti broj")
    quit()

a = list(a)
b = list(b)

a[1], b[1] = b[1], a[1]

print("".join(a))
print("".join(b))