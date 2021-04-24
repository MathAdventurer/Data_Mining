# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:42:36 2020

@author: Neal LONG
"""
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

def plot_mesh_labels(plt, model, x_min, x_max, y_min, y_max, step = 0.01):
    # plot the  labels of points predicted by model in the mesh area
    # [x_min, x_max]x[y_min, y_max] with plt.
   
    # Generate the points in in the mesh [x_min, x_max]x[y_min, y_max] with step size
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # merged into matrix of points, row <-> point
    mesh_points = np.c_[xx.ravel(), yy.ravel()]
    # predict the lables
    mesh_labels = model.predict(mesh_points)
    # reshape the labels to 1-d array
    mesh_labels_array = mesh_labels.reshape(xx.shape)

    # Put the result into a color plot
    
    plt.pcolormesh(xx, yy, mesh_labels_array, cmap=plt.cm.RdYlBu,shading='auto')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    
    
# Load data
iris = load_iris()

# We only take the first two corresponding features
X = iris.data[:, :2]
Y = iris.target

# Create an instance of DecisionTreeClassifier with all default parameters
tree = DecisionTreeClassifier()

#and fit the data.
tree.fit(X, Y)
Y_pred = tree.predict(X)
X_err = X[Y != Y_pred] # zero-one loss
print("There are {} errors/mismatches".format(sum(Y != Y_pred)))

# Plot the decision boundary. For that, we will assign a color to each
x_min = X[:, 0].min() - 0.5
x_max = X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
h = 0.01  # step size in the mesh


# Put the boundary with results of dense points' labels
plt.figure(1, figsize=(12, 12))
plot_mesh_labels(plt, tree, x_min ,x_max, y_min, y_max, 0.01)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.RdYlBu)
plt.scatter(X_err[:, 0], X_err[:, 1], marker='x', c='r', edgecolors='r')

plt.title("Decision surface of a decision tree ")
plt.axis("tight")

plt.show()