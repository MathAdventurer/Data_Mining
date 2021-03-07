# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:42:36 2020

@author: Neal LONG
"""
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Load data
iris = load_iris()

# Determine feature matrix X and taget array Y
X = iris.data[:,:2]
Y = iris.target

# Create and train decision tree on all 
clf = DecisionTreeClassifier()
clf.fit(X, Y)
# test the prediction
clf.predict([[1,1]])
print(iris.target_names)

# Plot tree structure
plt.figure(1, figsize=(12, 12))
plot_tree(clf, filled=True)
plt.show()



# Y != Y_pred
# scatter plot for the outcome