#coding=utf8
"""
Created on Tue Nov 07 18:00:12 2018

@author: Neal LONG
"""


from sklearn.datasets import load_iris


iris = load_iris()
print(iris.DESCR)
X, y = iris.data, iris.target
print("\n\nInformation of original X:")
print('Feature names:', iris.feature_names)
print('Feature matrix:type=',type(X),'shape=',X.shape)
print('Feature matrix:')
print(X)

print('Label vector:type=',type(y),'shape=',y.shape)
print('Label vector')
print(y)

#select first 3 rows/observations
X_subRow =X[0:3,:]
print("\nShape of X_subRow(first 3 rows)",X_subRow.shape)
print(X_subRow)
print(y[0:3])

#Select the from 4th rows until the end
X_subRowRemain =X[3:]
print("\nShape of X_subRow(after 3rd)",X_subRowRemain.shape)
print(X_subRowRemain)
print(y[3:])

#select last 3 rows/observations
X_subLastRow =X[-3:]
print("\nShape of X_subRow(last 3 rows)",X_subLastRow.shape)
print(X_subLastRow)
print(y[-3:])

#select first and third attributes(sepal length,and petal length  for iris data)
X_subColunm =X[:,[0,2]]
print("\nShape of X_subColunm(1st and 3rd attributes)",X_subColunm.shape)
print(X_subColunm)


#select first 2 attributes(sepal length,and sepal width for iris data)
X_subRowColunm =X_subRow[:,:2]
print("\nShape of X_subRowColunm(first 3 rows,first 2 attributes)",X_subRowColunm.shape)
print(X_subRowColunm)