# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:04:38 2020

@author: Neal LONG

Now we try to evalute the learning curve with 10-fold of three different models on X, y :
    1. RBF-SVM: SVC model with RBF kernel, gamma=0.001,  random_state=0 
    2. LinearSVC: LinearSVC model with random_state=0, C=0.001 
    3. DecisionTree: DecisionTreeClassifier model with  random_state=0
    
In particular, we are interested in the learning capacity of these models when we use 
10%,20%,30%,40%,50%,60%,70%,80%,90%,100% of all training examples

Note: 
    0. Set random_state=0
    1. 10-fold Stratified CV 
    2. Learning curve for givenTrainSizes from [10%,20%,30%,40%,50%,60%,70%,80%,90%,100%]
    3. Refer to 5-learning_curve.py
    4. Use accuracy as scoring metric
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC,LinearSVC
from sklearn.datasets import load_digits
from sklearn.model_selection import learning_curve
from sklearn.tree import DecisionTreeClassifier

def plot_learning_curve(estimator, title, X, y, givenTrainSizes, scoring = 'accuracy', cv = None):
    
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
    plt.ylim((0.5,1.1))

    
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")
    for xy in zip(train_sizes, test_scores_mean):                                       # <--
        ax.annotate('%s' % round(xy[1],2), xy=xy, textcoords='data')
    plt.legend(loc="best")
    plt.show()



digits = load_digits()
X, y = digits.data, digits.target

#++insert your code below++

givenTrainSizes = np.linspace(.1, 1.0, 10)

title = "Learning Curves (SVM, RBF kernel, $\gamma=0.001$)"
#SVC with RBF kernel (gamma=0.01)
estimator = SVC(gamma=0.001,random_state=0)
plot_learning_curve(estimator, title, X, y, givenTrainSizes, cv=10)

plt.show()

title = "Learning Curves (Linear SVM)"
#LinearSVC with C=0.001
estimator = LinearSVC(C=0.001,random_state=0)
plot_learning_curve(estimator, title, X, y, givenTrainSizes, cv=10)

plt.show()


title = "Learning Curves (Decision tree)"
#Decision tree with default settings
estimator = DecisionTreeClassifier(random_state=0)
plot_learning_curve(estimator, title, X, y, givenTrainSizes, cv=10)

plt.show()