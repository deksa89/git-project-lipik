import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Space_Race"
response = requests.get(url)

html = response.content
html_text = response.text

soup = BeautifulSoup(html, 'html.parser')
divs = soup.body.div.text

glavni_naslov = soup.find(id="firstHeading", class_="firstHeading")
print(glavni_naslov.text)

tekst_stranice = soup.find("div" ,id="mw-content-text").find_all("p")
#print(type(tekst_stranice))

lista_paragrafa = []
for i in tekst_stranice:
    lista_paragrafa.append(i.text)
#print(lista_paragrafa)

lista_podnaslova = []
podnaslovi = soup.find_all(class_="mw-headline")

for el in podnaslovi:
    lista_podnaslova.append(el.text)

print(lista_podnaslova)