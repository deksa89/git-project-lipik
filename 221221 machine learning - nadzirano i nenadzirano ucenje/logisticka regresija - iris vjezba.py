# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# from sklearn.datasets import load_iris
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix, classification_report
# from sklearn.preprocessing import StandardScaler
#
# iris_X, iris_y = load_iris(return_X_y=True)
#
# #iris_X = StandardScaler().fit_transform(iris_X)
#
# # data = load_iris(as_frame=True) #vraca pandas prikaz tablice
# # print(data.data)
#
# X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.15) #mala testna velicina
#
# clasiffier = LogisticRegression()
#
# clasiffier.fit(X_train, y_train)
# y_pred = clasiffier.predict(X_test)
#
# report = classification_report(y_test, y_pred)
# print(report)


# K-classification
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

iris_X, iris_y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.15) #mala testna velicina

clasiffier = KNeighborsClassifier(n_neighbors=5) #5 je po defaultu

clasiffier.fit(X_train, y_train)
y_pred = clasiffier.predict(X_test)

report_k_neighbors = classification_report(y_test, y_pred)
print(report_k_neighbors)