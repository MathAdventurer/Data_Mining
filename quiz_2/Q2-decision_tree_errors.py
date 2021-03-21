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
# print("This trained decision tree has {} nodes".format(clf.tree_.node_count))

# ++insert your code here++ to
# Create and train different decision tree with different tree depth
# then count error and corresponding total number of nodes


# Solution:

error = dict()
error_nodes = dict()

for i in range(1, 6):
    print(f"For the decision tree depth = {i}:")
    clf = DecisionTreeClassifier(criterion='entropy', random_state=0, max_depth=i)
    clf.fit(X, Y_true)
    Y_Pred = clf.predict(X)
    print("The zero-one loss is ", len(Y_true[Y_true != Y_Pred]))
    print("The number of nodes is ", clf.tree_.node_count)
    print("The number of errors + The number of nodes is ", len(Y_true[Y_true != Y_Pred]) + clf.tree_.node_count)
    error[i] = len(Y_true[Y_true != Y_Pred])
    error_nodes[i] = len(Y_true[Y_true != Y_Pred]) + clf.tree_.node_count
    # If want to get the visualization of the decision tree, run the following commented code.
    # plt.figure(1, figsize=(12, 12))
    # plot_tree(clf, filled=True)
    # plt.show()
    print("\n")

print("Answer for Q2:")

for i,v in error.items():
    if error[i] == min(error.values()):
        print(f"The best depth when the decision tree will generate minimum number of errors/mismatch is {i}")

for i, v in error_nodes.items():
    if error_nodes[i] == min(error_nodes.values()):
        print(f"The best depth when the decision tree generates minimum (number of errors + number of nodes) is {i}")
