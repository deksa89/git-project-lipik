
#najjednostavniji primjer

# import matplotlib.pyplot as plt
# import numpy as np
# import sklearn.linear_model as lm
#
# xtrain = np.array([[0],[1],[2]])
# ytrain = np.array([0, 1, 2])
#
#
# # plt.scatter(xtrain, ytrain)
# # plt.show()
#
# linear_model = lm.LinearRegression()
# linear_model.fit(xtrain, ytrain)
#
# # print(linear_model.coef_)  # nagib pravca i rjesenje je 1 jer je nabig pravca 1
# # print(linear_model.intercept_) # odsjecak na osi x
#
# xtest = np.array([[0.5], [3]])
# ypred = linear_model.predict(xtest)
#
# print(ypred)




import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score # <= mean squared error je mjera koja govori koliko dobro model radi
from sklearn.preprocessing import PolynomialFeatures

diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True) #vraca 2 izlazne velicine


# nrows, ncols = 2, 5
# fig = plt.figure()
# for i in range(1, 11):
#     ax = fig.add_subplot(nrows, ncols, i) #argument "i" krece od 1 te time prikazuje koji graf smo odabrali
#     ax.scatter(diabetes_X[:, i - 1], diabetes_y)
#
# plt.show()

diabetes_X = diabetes_X[:, 2] #kao primjer uzimamo treci graf
diabetes_X = diabetes_X[:, np.newaxis]

#dodali smo polinom 2 stupnja i prikazali s nepromjenjenom vrijednosti = diabetes_X_test[:,1], prije to ga je bio obican pravac
poly = PolynomialFeatures(degree=2)
diabetes_X = poly.fit_transform(diabetes_X) # iz jedne velicine dobijemo 3 sto nam daje tocnije rezultate

diabetes_X_train, diabetes_X_test, diabetes_y_train, diabetes_y_test = train_test_split(diabetes_X, diabetes_y, test_size=0.2) # iz x skupa cemo iscupati 20 posto za test, 80 posto za trening

linear_model = linear_model.LinearRegression()

linear_model.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_pred = linear_model.predict(diabetes_X_test)

mse = mean_squared_error(diabetes_y_test, diabetes_y_pred)
#print(mse)


r2 = r2_score(diabetes_y_test, diabetes_y_pred)
print(r2)

plt.scatter(diabetes_X_test[:,1], diabetes_y_test)
plt.scatter(diabetes_X_test[:,1], diabetes_y_pred, color="red")
plt.show()

# plt.scatter(diabetes_X_test, diabetes_y_test)
# plt.plot(diabetes_X_test, diabetes_y_pred, color="red", marker="v") #marker mozes biti o, x, v, plot crta prediction kroz nas scatter
#
# plt.show()















