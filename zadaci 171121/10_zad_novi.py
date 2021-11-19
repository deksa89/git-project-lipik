#10. S tipkovnice učitajte proizvoljni niz znakova. Kreirajte novi niz znakova koji će sadržavati naizmjence velika i mala slova iz ulaznog
#niza, redom kako se pojavljuju u ulaznom nizu: prvo upper_case slovo u ulaznom nizu, prvo sljedeće malo slovo u nastavku ulaznog niza,
#prvo sljedeće upper_case slovo u nastavku ulaznog niza itd. Novokreirani niz ispišite na zaslon. U nastavku se nalazi primjer:
#Ulazni niz: ifeFemFEkej83FkW ,  Izlazni niz: FeFkFkW

str_a = "ifeFemFEkej83FkW"

new = ""
upper_case = True

for i in str_a:
    if "A" < i < "Z" and upper_case == True:
        new += i
        upper_case = False
    elif "a" < i < "z" and upper_case == False:
        new += i
        upper_case = True

print(new)