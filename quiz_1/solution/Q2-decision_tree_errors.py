# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:30:42 2020

@author: Neal LONG

count the zero-one loss of decision tree with different max_depth 
from [1,2,3,4,5], but random_state is always set to 0 
"""


from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load data
iris = load_iris()

# Determine feature matrix X and target array Y
X = iris.data
Y_true = iris.target
clf = DecisionTreeClassifier()
clf.fit(X, Y_true)
Y_Pred = clf.predict(X)
print("This trained decision tree has {} nodes".format(clf.tree_.node_count))


# Create and train different decision tree with different tree depth
# then count error and corresponding total number of nodes
scores = []
for d in [2,3,4,5,6,7,8,9,10]:
    clf = DecisionTreeClassifier(max_depth=d,random_state=0)
    clf.fit(X, Y_true)
    Y_Pred = clf.predict(X)
    scores.append((d,sum(Y_Pred!=Y_true),sum(Y_Pred!=Y_true)+clf.tree_.node_count))
    
print("Tree with depth ={} has minimum errors ".format(sorted(scores,key=lambda x:x[1])[0][0]))
print("Tree with depth ={} has minimum errors + number of nodes ".format(sorted(scores,key=lambda x:x[2])[0][0]))