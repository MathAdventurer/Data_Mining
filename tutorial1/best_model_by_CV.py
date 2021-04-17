#coding=utf8
"""
Created on Sun Nov 12 22:42:54 2017

@author: Neal LONG
"""

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, cross_val_score, StratifiedKFold
import numpy as np
iris = datasets.load_iris()
X= iris.data
y= iris.target


kfold_cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=0)

# conduct 10-fold cv to select best model parameters
print("\nConduct 10 fold cross-validation to select best model parameters")
params = {'C':[0.0001,1,1000]}
bestModel = GridSearchCV(LogisticRegression(solver = 'liblinear'), params, scoring='accuracy',cv=kfold_cv)
bestModel.fit(iris.data, iris.target)
print("\nThe best model parameter C in LogisticRegressionfor is {} with accuracy is {}".format(bestModel.best_params_['C'],bestModel.best_score_))
#We can directly use it to predict the unseen data
print('Predict Results of [[1,2,3,4]] is',bestModel.predict([[1,2,3,4]]))

#This is equivilant to mannually trained model with best parameter C=1000
bestModel_mannual = LogisticRegression(C=1000, solver = 'liblinear')
print("\nThe  logistic model trained with parameter C =1000 has accuracy= {}".format(np.mean(cross_val_score(bestModel_mannual,iris.data, iris.target,cv=kfold_cv))))
bestModel_mannual.fit(iris.data, iris.target)
print('Predict Results of [[1,2,3,4]] is',bestModel_mannual.predict([[1,2,3,4]]))
