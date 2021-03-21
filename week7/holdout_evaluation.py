#coding=utf8
"""
Created on Tue Nov 7 21:18:55 2018

@author: Neal LONG

Reference:
    https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
    https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
"""

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np

y_pred = [0, 2, 1, 3, 2]
y_true = [0, 1, 2, 3, 2]
print(accuracy_score(y_true, y_pred))
print(accuracy_score(y_true, y_pred, normalize=False))
print("="*30)

X = np.arange(10).reshape((5, 2))
y =  np.arange(5)
print('X=\n',X)
print('y=', y)

print("\n0","="*30)
test_ratio = 0.4
train_index = round((1-test_ratio)*len(X))
X_train = X[:train_index,:]
y_train = y[:train_index]
X_test = X[train_index:,:]
y_test = y[train_index:]
print('X_train =\n', X_train)
print("y_train = ", y_train)
print('X_test =\n', X_test)
print("y_test = ", y_test)

print("\n1","="*30)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                    test_size=0.4, shuffle=False)
print('X_train =\n', X_train)
print("y_train = ", y_train)
print('X_test =\n', X_test)
print("y_test = ", y_test)

print("\n2","="*30)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                    test_size=0.4)
print('X_train =\n', X_train)
print("y_train = ", y_train)
print('X_test =\n', X_test)
print("y_test = ", y_test)

print("\n3","="*30)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                    test_size=0.4)
print('X_train =\n', X_train)
print("y_train = ", y_train)
print('X_test =\n', X_test)
print("y_test = ", y_test)

print("="*30)
print("Play with Iris Data ")
print("="*30)
iris = datasets.load_iris()
X= iris.data
y= iris.target

#create a Logistic Regression model with specified  parameters
clf = LogisticRegression(solver = 'newton-cg',multi_class= 'auto')

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                            test_size=0.2, shuffle=False)
clf.fit(X_train, y_train)  
y_train_pred = clf.predict(X_train)
y_test_pred = clf.predict(X_test)


print("\nThe in_performance is ",accuracy_score(y_train_pred, y_train))
print("The out_performance is ",accuracy_score(y_test_pred, y_test))