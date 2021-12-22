#uvod u logisticku regresiju

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

X_train = np.array([[1],[2],[3],[4],[5],[6]])
y_train = np.array([0, 0, 0, 1, 1, 1])

# plt.scatter(X_train, y_train)
# plt.show()

classifier = LogisticRegression()
classifier.fit(X_train, y_train)

X_test = np.array([[2.5],[3.9]])
y_test = np.array([0, 1])

y_pred = classifier.predict(X_test)
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix) # [[1 0] [0 1]] to znaci da je 3.9 predvideno kao 1 a 2.5 kao 0

report = classification_report(y_test, y_pred) # f1-score je kombinacija precision-a i recall-a i uzima se kao najbolja vrijednost
print(report)



