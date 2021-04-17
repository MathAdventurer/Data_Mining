# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:31:51 2020

@author: Neal LONG
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

def plot_learning_curve(estimator, title, X, y, givenTrainSizes, scoring = 'accuracy', cv = None):
    """
    Generate a simple plot of the test and training learning curve.

    Parameters
    ----------
    estimator : object type that implements the "fit" and "predict" methods
        An object of that type which is cloned for each validation.

    title : string
        Title for the chart.

    X : array-like, shape (n_samples, n_features)
        Training vector, where n_samples is the number of samples and
        n_features is the number of features.

    y : array-like, shape (n_samples) or (n_samples, n_features), optional
        Target relative to X for classification or regression;
        None for unsupervised learning.

    scoring : string, callable or None, optional, default: None
              A string (see model evaluation documentation) or
             a scorer callable object / function with signature scorer(estimator, X, y).

    cv : int, cross-validation generator or an iterable, optional
         Determines the cross-validation splitting strategy.
         Possible inputs for cv are:
          - None, to use the default 5-fold Stratified cross-validation,
          - integer, to specify the number of folds for Stratified  cross-validation
          - An object to be used as a cross-validation generator.
          - An iterable yielding train/test splits.
          
    givenTrainSizes : list, defines different percentages of whole train data used to 
                  evaluate learning capacity

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.

    """
    fig =  plt.figure(1, figsize=(6, 6))
    ax = fig.add_subplot(111)

    plt.title(title)
    plt.xlabel("Training examples")
    plt.ylabel("Accuracy")
   
    
    # read the help of learning_curve, and call learning_curve with proper paramters
    train_sizes, train_scores, test_scores = learning_curve(estimator,X,y,
                                                            scoring=scoring,
                                                            cv=cv,
                                                            train_sizes=givenTrainSizes,
                                                            random_state=0)
    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    plt.grid()

    
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")
    for xy in zip(train_sizes, test_scores_mean):                                       # <--
        ax.annotate('%s' % round(xy[1],2), xy=xy, textcoords='data')
    plt.legend(loc="best")
    plt.show()

iris = load_iris()

# Determine feature matrix X and taget array Y
X = iris.data[:,:2]
y = iris.target
basic_clf = DecisionTreeClassifier(random_state=0)
title = "Learning Curves (DecisionTreeClassifier)"

givenTrainSizes = np.linspace(.1, 1.0, 5)
# 5-fold Stratified CV for train example with percentage of training data from  
# givenTrainSizes =[0.1  , 0.325, 0.55 , 0.775, 1.   ]
plot_learning_curve(basic_clf, title, X, y, givenTrainSizes, scoring='accuracy', cv=5)

