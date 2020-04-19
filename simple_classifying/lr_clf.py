import numpy as np
import csv

from sklearn import linear_model
from sklearn.model_selection import train_test_split

X = np.loadtxt('data.csv', delimiter=',')
Y = np.loadtxt('labels.csv', delimiter=',')
X = np.array(X).reshape(-1,1)
Y = np.array(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

clf_lr = linear_model.LogisticRegression()
clf_lr.fit(X_train, Y_train)

print("accuracy of training data:", clf_lr.score(X_train, Y_train))
print("accuracy of testing data:", clf_lr.score(X_test, Y_test))
