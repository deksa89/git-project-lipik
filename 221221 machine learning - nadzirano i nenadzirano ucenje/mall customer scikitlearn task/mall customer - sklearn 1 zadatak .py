# 1.Zadatak - Učitajte Mall_Customers.csv podatke. Koristeći Spending_score veličinu, te jednu veličinu po
#izboru odredite centre klastera koristeći Kmeans algoritam.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


data = pd.read_csv("Mall_Customers.csv")

X = data.iloc[:, [3,4]].values
#print(X)
# print(y)
#df = pd.DataFrame(data)
#print(df.head())

#X = np.array([])

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

print(kmeans.cluster_centers_)




