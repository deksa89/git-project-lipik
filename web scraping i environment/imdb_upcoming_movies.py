import pandas as pd
import numpy as np

import requests
from requests import get
from bs4 import BeautifulSoup

from time import sleep
from random import randint

import re

#creating the lists that we want to append scraped info into:
titles = []
years = []
run_time_mins = []
genre = []
director = []

#getting the content from url:
page = requests.get('https://www.imdb.com/movies-coming-soon/?ref=nv_mv_cs')
soup = BeautifulSoup(page.text, 'html.parser')

#scraping for the data we are looking for
group_div_odd = soup.find_all("div", class_="list_item odd")
for container_odd in group_div_odd:
    name = container_odd.h4.a.text
    name = name.split(" ")
    titles.append(" ".join(name[:-1]))

    name1 = container_odd.h4.a.text
    name1 = name1.split(" ")
    years.append("".join(name1[-1][1:-1]))


    trajanje = container_odd.find_all("time") if container_odd.find("time") else '-'
    for tm in trajanje[0]:
        run_time_mins.append(tm)

    zanr = container_odd.find("span")
    for zr in zanr:
        genre.append(zr)

    rezija = container_odd.find("div", class_="txt-block").find("span").text
    director.append(rezija)



group_div_even = soup.find_all("div", class_="list_item even")
for container_even in group_div_even:
    name2 = container_even.h4.a.text
    name2 = name2.split(" ")
    titles.append(" ".join(name2[:-1]))

    name3 = container_even.h4.a.text
    name3 = name3.split(" ")
    years.append("".join(name3[-1][1:-1]))

    trajanje1 = container_even.find_all("time") if container_even.find("time") else '-'
    for i in trajanje1[0]:
        run_time_mins.append(i)

    zanr1 = container_even.find("span")
    for zr1 in zanr1:
        genre.append(zr1)

    rezija1 = container_even.find("div", class_="txt-block").find("span").text
    director.append(rezija1)

#Creating the dataset:
movies = pd.DataFrame({'Movie': titles,
                        'Year': years,
                        'Length(minutes)': run_time_mins,
                        'Genre': genre,
                        'Director': director})

#Cleaning messy strings within pandas DataFrame:
movies["Director"] = movies["Director"].str.replace(r'\n',' ', regex=True)
movies['Director'] = movies['Director'].map(lambda x: x.rstrip(' '))


#Creating the cvs file from our dataset
movies.to_csv('imdb_upcoming_movies.csv')
