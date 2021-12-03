import pandas as pd

data = pd.read_csv("letovi.csv", index_col=0)
#print(data.head())


#1. Loadaj Deanovu tablicu (pazi na header)
#print(data.shape)

#print(data.size)

#print(data.describe())


#2. Prikaži podatke o tablici
    # (koje metode ćete koristiti uvijek za dataframeove o kojima ne znate ništa?)

data.dropna(inplace=True)

# new data frame with split value columns
new = data["Prices"].str.split(" ", n=1, expand=True)

# making separate first name column from new data frame
data["value"] = new[0]

# making separate last name column from new data frame
data["currency"] = new[1]

# Dropping old Name columns
data.drop(columns=["Prices"], inplace=True)

# df display
print(data.describe())


for i, row in data.iterrows():
    euri = round((float(row["value"].replace(".", "")) / 7.4),2)
    #print(euri)

    data.at[i, "value"] = euri
    data.at[i, "currency"] = "EUR"

#4 zadatak s datetime, python calculates date difference

print(data.head())
