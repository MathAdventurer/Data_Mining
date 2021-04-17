# # -*- coding: utf-8 -*-
# """
# Created on Sat Mar 21 21:00:09 2020
#
# @author: Neal LONG
#
#
# Advantages of using validation_curve:
#     0. Less code
#     1. Concurrent execution with n_jobs >1
#     2. Detailed  train and test scores for every fold and every model
#
# """
#
# from sklearn.datasets import load_iris
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import cross_val_score,train_test_split,validation_curve
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.metrics import accuracy_score
#
# # Load data
# iris = load_iris()
#
# # Determine feature matrix X and taget array Y
# X = iris.data[:,:2]
# y = iris.target
# candidate_max_depth = [1,2,3,4,5,6]
#
#
# ##########
# X_train, X_test, y_train, y_test = train_test_split(X, y,
#                                                 test_size=0.4, random_state= 0)
# in_performance = []
# out_performance = []
# max_depths = [1,2,3,4,5,6]
# for d in max_depths:
#     clf = DecisionTreeClassifier(max_depth=d,random_state=0)
#     clf.fit(X_train, y_train)
#     y_train_pred = clf.predict(X_train)
#     y_test_pred = clf.predict(X_test)
#     in_performance.append(accuracy_score(y_train_pred, y_train))
#     out_performance.append(accuracy_score(y_test_pred, y_test))
#
# plt.figure(1, figsize=(8, 8))
# plt.plot(candidate_max_depth, in_performance,marker='o',label="Training Acc.",
#              color="darkorange")
# plt.plot(candidate_max_depth, out_performance,marker='o',label = "Holdout Acc.",
#              color="navy")
# plt.ylabel("Accuracy")
# plt.xlabel("max_depth")
# plt.title('Choose best max_depth with singel holdout split')
#
# plt.grid(True)
# plt.legend()
# plt.show()
#
#
#
# ##########
# out_performance = []
# in_performance = []
#
# for d in candidate_max_depth:
#     clf = DecisionTreeClassifier(max_depth=d, random_state=0)
#     cv_scores = cross_val_score(clf, X, y, cv=5,
#                                 scoring='accuracy')
#     out_performance.append(np.mean(cv_scores))
# plt.figure(1, figsize=(8, 8))
# plt.ylabel("Accuracy")
# plt.xlabel("max_depth")
# plt.plot(candidate_max_depth, out_performance,color="navy",marker='o',
#          label = "Mean test Acc. from 5-fold CV")
# plt.grid(True)
# plt.legend()
# plt.title('5-fold CV Curve for Decision Tree on max_depth by cross_val_score')
# plt.show()
#
#
# ##########
#
#
# base_clf = DecisionTreeClassifier(random_state=0)
# train_scores, test_scores = validation_curve( base_clf, X, y, param_name="max_depth",
#     param_range=candidate_max_depth, scoring="accuracy", n_jobs=-1, cv =5)
# train_scores_mean = np.mean(train_scores, axis=1)
# test_scores_mean = np.mean(test_scores, axis=1)
# plt.figure(1, figsize=(8, 8))
# plt.ylabel("Accuracy")
# plt.xlabel("max_depth")
# plt.title("K-fold(k={}) CV Curve for Decision Tree on max_depth by validation_curve".format(train_scores.shape[1]))
#
# plt.plot(candidate_max_depth, train_scores_mean,marker='o',label="Mean training Acc. from 5-fold CV",
#              color="darkorange")
# plt.plot(candidate_max_depth, test_scores_mean,marker='o',label="Mean test Acc. from 5-fold CV",
#              color="navy")
# plt.grid(True)
# plt.legend()
# plt.show()
#
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:30:33 2020

@author: Neal LONG
Ref:
    1.SVC: https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
    2.validation_curve: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html
    3.plt.semilogx: https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.pyplot.semilogx.html

Note:
    0. Set random_state=0
    1. Use plt.semilogx to plot the training/Cross-validation score curve since
       range of gamma in gamma_candidates varies among different scales
    2. In title of the plot, shows the number of k for adopted K-fold
       as 3-validation_curve.py
   3. Use accuracy as scoring metric


"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=10)

X, y = load_digits(return_X_y=True)
gamma_candidates = np.logspace(-6, -1, 5)

# Run validation_curve(), and get the 10-fold Stratified cross-validations,
# and get train/test accuracy score for SVC model with random_state=0, and
# different gammas from gama_candidates defined as above
# Finally plot the validation curve of SVC among different gamma


# ++insert your code below++
skf = StratifiedKFold(n_splits=10)
train_scores, test_scores = validation_curve(
    SVC(), X, y, param_name="gamma", param_range=gamma_candidates,
    scoring="accuracy", n_jobs=-1, cv=skf)

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

plt.figure(1, figsize=(8, 8))
plt.title("K-fold(k=10) Validation Curve with SVM")
plt.xlabel(r"$\gamma$")
plt.ylabel("Score")
plt.ylim(0.0, 1.1)
lw = 2

plt.semilogx(gamma_candidates, train_scores_mean, label="Mean training Acc. from 10-fold CV",
             color="darkorange", lw=lw)

plt.semilogx(gamma_candidates, test_scores_mean, label="Mean test Acc. from 10-fold CV",
             color="navy", lw=lw)
plt.legend(loc="best")
plt.grid(True)
plt.show()
plt.savefig('Q1_Validation_Curve.png')
