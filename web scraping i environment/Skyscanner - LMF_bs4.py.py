import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
from requests import get

from time import sleep
from random import randint

import re

departure_location = []
destination = []
price = []
airline = []
departure_date = []
date_of_arrival = []


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
response = requests.get("https://www.skyscanner.net/hr/en-gb/hrk/flights/last-minute-deals/?", headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# print(response.content)

group_div = soup.find_all("div", id="flight-deals-root")
for container in group_div:
    cijena = container.find_all("span", class_="BpkText_bpk-text__1KKbW BpkText_bpk-text--lg__212sq DealCard_DealCard__price__1O9CP")
    for cj in cijena:
        price.append(cj.text)

    avio = container.find_all("span",class_="BpkText_bpk-text__1KKbW BpkText_bpk-text--xs__11Wpt DealCard_DealCard__carrier__2Sox7")
    for tekst in avio:
        airline.append(tekst.text)

    datum = container.find_all("span", class_="BpkText_bpk-text__1KKbW BpkText_bpk-text--base__1zXAn Leg_Leg__date__3PXsE")
    for j, dat in enumerate(datum):
        if j % 2 == 0:
            departure_date.append(dat.text)
        else:
            date_of_arrival.append(dat.text)

    cilj = container.find_all("span", class_="BpkText_bpk-text__1KKbW BpkText_bpk-text--base__1zXAn")
    lista = []
    for i, c in enumerate(cilj):
        c = c.text
        lista.append(c)

    svaki1 = lista[::4]
    for i in svaki1:
        departure_location.append(i)
    svaki3 = lista[2::4]
    for j in svaki3:
        destination.append(j)

print(price)
#print(airline)
#print(departure_date)
#print(date_of_arrival)
# print(departure_location)
# print(destination)

red_letenja = pd.DataFrame({
            "Zracna luka polaska" : departure_location,
            "Zracna luka destinacije" : destination,
            "Datum polaska" : departure_date,
            "Datum dolaska" : date_of_arrival,
            "Cijena karte" : price,
            "Avioprijevoznik" : airline})

#print(red_letenja.head())

#red_letenja.to_csv('red_letenja.csv')
