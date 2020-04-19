import numpy as np
import csv

from sklearn import svm
from sklearn.model_selection import train_test_split

X = np.loadtxt('data.csv', delimiter=',')
Y = np.loadtxt('labels.csv', delimiter=',')
X = np.array(X).reshape(-1,1)
Y = np.array(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

clf_svm = svm.SVC()
clf_svm.fit(X_train, Y_train)

print("accuracy of training data:", clf_svm.score(X_train, Y_train))
print("accuracy of testing data:", clf_svm.score(X_test, Y_test))
