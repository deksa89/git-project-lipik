import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
import graphviz


data_iris = load_iris()

X = data_iris.data
y = data_iris.target
print(len(X))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# clf_decision = DecisionTreeClassifier(criterion="entropy")
# clf_regression = DecisionTreeRegressor()
#
# clf_regression.fit(X_train, y_train)
#
# print('preciznost na trening podacima je:', accuracy_score(y_true=y_train, y_pred=clf_regression.predict(X_train)))
# print('preciznost na test podacima je:', accuracy_score(y_true=y_test, y_pred=clf_regression.predict(X_test)))


model = RandomForestClassifier(n_estimators=80)
model.fit(data_iris.data, data_iris.target)
estimator = model.estimators_[5]

print('preciznost na trening podacima je:', accuracy_score(y_true=y_train, y_pred=estimator.predict(X_train)))
print('preciznost na test podacima je:', accuracy_score(y_true=y_test, y_pred=estimator.predict(X_test)))

dot_data = tree.export_graphviz(estimator, out_file=None,
                                feature_names=data_iris.feature_names,
                                class_names=data_iris.target_names,
                                filled=True)

# Draw graph
graph = graphviz.Source(dot_data, format="png")
graph.render("decision_tree_graphivz-random_state, data_iris")