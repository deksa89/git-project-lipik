#creating a classification model by building a decision tree and regression tree and ploting the result using graphviz
import graphviz
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree


data_wine = load_wine()

X = data_wine.data
y = data_wine.target

print(len(X))
print(len(y))

## This one is an example of Decision Tree Classifier:
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
#
# clf_decision = DecisionTreeClassifier()
# clf_decision.fit(X_train, y_train)
#
#
# print("decision tree classifier, preciznost na trening podacima: ", accuracy_score(y_true=y_train, y_pred=clf_decision.predict(X_train)))
# print("decision tree classifier ,preciznost na test podacima: ", accuracy_score(y_true=y_test, y_pred=clf_decision.predict(X_test)))


## This one is an example of Decision Tree Regressor:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

clf_regression = DecisionTreeRegressor()

clf_regression.fit(X_train, y_train)

print("regressor tree classifier ,preciznost na trening podacima: ", accuracy_score(y_true=y_train, y_pred=clf_regression.predict(X_train)))
print("regressor tree classifier ,preciznost na test podacima: ", accuracy_score(y_true=y_test, y_pred=clf_regression.predict(X_test)))


#drawing a graph
dot_data = tree.export_graphviz(clf_regression, out_file=None,
                                feature_names=data_wine.feature_names,
                                class_names=data_wine.target_names,
                                filled=True)

# Draw graph
graph = graphviz.Source(dot_data, format="png")
graph.render("regression_tree, data_wine")


## This one is an example of Random Forest Classifier:
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)

classifier = RandomForestClassifier(n_estimators=600 ,max_depth=2, random_state=0)
classifier.fit(X_train , y_train)
#estimator = classifier.estimators_[4]

y_pred = classifier.predict(X_test)

from sklearn.metrics import precision_score
rezultat = accuracy_score(y_test, y_pred)
print("tocnost predikcije koristeci Random Forest Classifier algoritam: ", rezultat)




