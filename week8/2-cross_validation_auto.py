# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:10:42 2020

@author: Neal LONG
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score,cross_validate
from sklearn.model_selection import StratifiedKFold
import numpy as np
# Load data
iris = load_iris()

# Determine feature matrix X and taget array Y
X = iris.data[:,:2]
y = iris.target
clf = DecisionTreeClassifier(max_depth=4,random_state=0)
skf = StratifiedKFold(n_splits=5)


print('Manually CV score')    
test_accs = []
for train_index, test_index in skf.split(X, y):
     X_train, X_test = X[train_index], X[test_index]
     y_train, y_test = y[train_index], y[test_index]
     clf.fit(X_train, y_train)  
     y_test_pred = clf.predict(X_test)
     test_accs.append(accuracy_score(y_test_pred, y_test))
print('The mean accuracy on test data in mannual 5-fold CV is', np.mean(test_accs))     
 
print('\nAutomatic CV score in sklearn')   
cv_scores = cross_val_score(clf, X, y, cv=skf,scoring="accuracy")
cv_scores_1 = cross_val_score(clf, X, y, cv=5,scoring="accuracy")
print('The mean accuracy of cross_val_score automatically is', np.mean(cv_scores))

print('\nMore information in cross_validate')   
cv_results = cross_validate(clf, X, y, cv=5,scoring="accuracy")
print(cv_results)
print('The mean accuracy in cross_validate', np.mean(cv_results['test_score'])) 

