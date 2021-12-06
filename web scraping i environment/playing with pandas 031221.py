import pandas as pd
import re
import numpy as np

#1. Loadaj tablicu
#2. Prikaži podatke o tablici
    # (koje metode ćete koristiti uvijek za dataframeove o kojima ne znate ništa?)
data = pd.read_csv("letovi.csv", index_col=0)
#print(data.head())
#print(data.shape)
#print(data.size)
#print(data.describe())


# 3. Pretvori column sa cijenama u dva nova:
    # a) numeričke vrijednosti (napravi konverzije u EUR ili bilo koju drugu valutu)
    # b) drugi stupac gdje piše valuta
data.dropna(inplace=True)

new = data["Prices"].str.split(" ", n=1, expand=True)
data["value"] = new[0]
data["currency"] = new[1]

data.drop(columns=["Prices"], inplace=True)

# df display
#print(data.describe())

#make two new colums, one with prices in euro and other with currency names
for i, row in data.iterrows():
    euri = round((float(row["value"].replace(".", "")) / 7.4),2)

    data.at[i, "Value"] = euri
    data.at[i, "Currency"] = "EUR"

#print(data.head())
#data.to_csv('izmjenjena tablica.csv')


# 4. Dodajte novi stupac gdje piše trajanje putovanja (arrival minus departure)
    # stavite 1h ako je trajanje dana 0

#pull out the list of strings out of colum "Departure date" and unpack them to depar list
#to be able to subtract them later
depar = []
for j, row1 in data.iterrows():
    dep = re.findall(r'\d+', row1["Departure date:"])
    for d in dep:
        if type(d) is list:
            for item in d:
                depa.append(int(item))
        else:
            depar.append(int(d))


#pull out the list of strings out of colum "Date of Arrival" and unpack them to ariva list
#to be able to subtract them later
ariva = []
for k, row2 in data.iterrows():
    ari = re.findall(r'\d+', row2["Date of Arrival:"])
    for a in ari:
        if type(a) is list:
            for item in a:
                ariva.append(int(item))
        else:
            ariva.append(int(a))


#find the difference between departure and arrival dates
difference = []
result = zip(ariva, depar)
for ariva, depar in result:
    if ariva - depar < 0:
        difference.append(depar - ariva)
    else:
        difference.append(ariva - depar)
difference = ["1h" if x==0 else x for x in difference]

#appending the column holiday duration which shows us a difference between each departure and arrival date
data["holiday duration"] = difference


# 5. Pronađi najpovoljni let srijedom
    # iterrows()
    # sort_values()
    # group_by()

#Creating a new column with splitted departure days, since it's easier to manipulate with those columns
data[["Day","Date", "Month"]] = data["Departure date:"].str.split(expand=True)
#print(data.head())

#Grouping out flights by days of week
po_danima= data.groupby("Day")
#print(po_danima.size())

#Getting a group with flights on Wednesday
sri_grupa = po_danima.get_group("Wed")
#print(sri_grupa)

#puling out minimum and maximum price on Wednesdays
najjeftinije_najskuplje = sri_grupa.Value.agg(['min', 'max'])
print(najjeftinije_najskuplje)





