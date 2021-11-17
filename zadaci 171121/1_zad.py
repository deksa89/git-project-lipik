#1. Napiši program koji učitava listu i briše sve duplikate iz te liste te ispisuje novu listu s 
#obrisanim duplikatima.

a = [1,2,3,4,3,2,1,4,2,1,2]

def duplicate(a):
    nova = []
    for i in a:
        if i not in nova:
            nova.append(i)
    return nova

print(duplicate(a))