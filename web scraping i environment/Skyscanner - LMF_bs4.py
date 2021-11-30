import pandas as pd
import numpy as np

import requests
from requests import get
from bs4 import BeautifulSoup

from time import sleep
from random import randint

import re


destination = []
price = []
airline = []
departure_date = []
date_of_arrival = []


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
response = requests.get("https://www.skyscanner.net/hr/en-gb/hrk/flights/last-minute-deals/", headers=headers)
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

print(price)

