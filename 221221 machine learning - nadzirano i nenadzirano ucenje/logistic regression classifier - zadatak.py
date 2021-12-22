import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("heart.csv")

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
# print(x)
# print(y)
df = pd.DataFrame(data)
#print(df)

# Izgradite klasifikator koristeći logističku regresiju čiji je izlaz binarna vrijednost koja označava
# postoji li šansa za srčani udar na temelju informacija / nalaza pacijenta zapisanih u heart.csv
# datoteci.

X = StandardScaler().fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

conf_matrix1 = confusion_matrix(y_test, y_pred)
report1 = classification_report(y_test, y_pred)

print(conf_matrix1)
print(report1)



#Ponovite prethodni zadatak koristeći metodu K najbližih susjeda. Koristite više ulaznih veličina, interpretirajte rezultate.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clasiffier = KNeighborsClassifier(n_neighbors=5)

clasiffier.fit(X_train, y_train)
y_pred = clasiffier.predict(X_test)

conf_matrix = confusion_matrix(y_test, y_pred)
report_k_neighbors = classification_report(y_test, y_pred)

print(conf_matrix)
print(report_k_neighbors)