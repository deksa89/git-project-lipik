"""15. Omogućite unos niza znakova te ispišite sljedeće:
	a) svaka neparna riječ (osim prve) iz niza mora biti ispisana malim znakovima po redu kako su bili unešeni
	b) svaka parna riječ (osim posljednje parne) iz niza mora biti ispisana velikim znakovima, obrnutim redom od onog kako je bila unešena"""

x = "ja sam samo mali covjek na ovome svijetu".upper()
x = x.split(" ")

string = []
for i in x:
    if len(i) % 2 == 0:
        string.append(i)
    elif len(i) % 2 != 0:
        string.append(i.lower())


spojeno = " ".join(string)
izmjenjeno = spojeno

print(izmjenjeno)

#output: JA sam SAMO MALI COVJEK NA ovome svijetu => neznam kako da iz for loopa izvucem prvi/zadnji element i ostavim ga nepromjenjen