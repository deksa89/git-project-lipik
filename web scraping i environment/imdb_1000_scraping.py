import pandas as pd
import numpy as np

import requests
from requests import get
from bs4 import BeautifulSoup

from time import sleep
from random import randint

titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

headers = {'Accept-Language': 'en-US, en;q=0.5'}

pages = np.arange(1, 1001, 50)

for page in pages:
    page = requests.get('https://www.imdb.com/search/title/?groups=top_1000&start=' + str(page) + '&ref_=adv_nxt', headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    movie_div = soup.find_all("div", class_="lister-item mode-advanced")

    sleep(randint(2,10))

    for container in movie_div:
        name = container.h3.a.text
        titles.append(name)

        year = container.h3.find("span", class_="lister-item-year text-muted unbold" ).text
        years.append(year)

        length = container.find("span", class_="runtime").text if container.p.find('span', class_='runtime') else '-'
        time.append(length)

        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        m_score = container.find("span", class_="metascore").text if container.find('span', class_='metascore') else '-'
        metascores.append(m_score)

        nv = container.find_all("span", attrs={'name':'nv'})
        vote = nv[0].text
        votes.append(vote)

        grosses = nv[1].text if len(nv) > 1 else "-"
        us_gross.append(grosses)
