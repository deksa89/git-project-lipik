import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

housing_X, housing_y = datasets.fetch_california_housing(return_X_y=True)

# nrows, ncols = 3, 3
# fig = plt.figure()
# for i in range(1, 9):
#     ax = fig.add_subplot(nrows, ncols, i)
#     ax.scatter(housing_X[:, i - 1], housing_y)

#plt.show()

housing_X = housing_X[:,0]
housing_X = housing_X[:, np.newaxis]


poly = PolynomialFeatures(degree=3)
diabetes_X = poly.fit_transform(housing_X)



housing_X_train, housing_X_test, housing_y_train, housing_y_test = train_test_split(housing_X, housing_y, test_size=0.3)

linear_model = linear_model.LinearRegression()

linear_model.fit(housing_X_train, housing_y_train)

housing_y_pred = linear_model.predict(housing_X_test)

mse = mean_squared_error(housing_y_test, housing_y_pred)
# print(mse)
#
# r2 = r2_score(housing_y_test, housing_y_pred)
# print(r2)


print(linear_model.coef_)
print(linear_model.intercept_)

#linear regression
# plt.scatter(housing_X_test, housing_y_test)
# plt.plot(housing_X_test, housing_y_pred, color="red", marker="v") #marker mozes biti o, x, v, plot crta prediction kroz nas scatter
#plt.show()


#polynomial features plot
# plt.scatter(housing_X_test, housing_y_test)
# plt.plot(housing_X_test, housing_y_pred, color="red", marker="v") #marker mozes biti o, x, v, plot crta prediction kroz nas scatter
#
# plt.show()