import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_covtype
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn import tree
import graphviz

data_covtype = fetch_covtype()
data_iris = load_iris()

X = data_covtype.data
y = data_covtype.target
print(len(X))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

#clf = DecisionTreeClassifier(criterion="entropy") # entropy = poboljsava preciznost na testnim podacima
clf = DecisionTreeRegressor() # 7.) daje malo losije podatke nego klasifikacijski model u ovom slucaju
clf.fit(X_train, y_train)

#y_pred = clf.predict(X_test)


print('preciznost na trening podacima je:', accuracy_score(y_true=y_train, y_pred=clf.predict(X_train)))
print('preciznost na test podacima je:', accuracy_score(y_true=y_test, y_pred=clf.predict(X_test)))

model = RandomForestClassifier(n_estimators=10)
model.fit(data_covtype.data, data_covtype.target)
estimator = model.estimators_[5]

dot_data = tree.export_graphviz(estimator, out_file=None,
                                feature_names=data_covtype.feature_names,
                                class_names=data_covtype.target_names,
                                filled=True)

# Draw graph
graph = graphviz.Source(dot_data, format="png")
graph.render("decision_tree_graphivz-random_state, fetch_covtype")





# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)
#
# from sklearn.ensemble import RandomForestClassifier
# classifier = RandomForestClassifier()
# classifier.fit(X_train, y_train)
# y_pred = classifier.predict(X_test)
#
# from sklearn.metrics import accuracy_score
# rezultat=accuracy_score(y_test,y_pred)
# print("accuracy score is:", rezultat)

