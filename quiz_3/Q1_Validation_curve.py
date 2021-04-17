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


#++insert your code below++
skf = StratifiedKFold(n_splits=10)
train_scores, test_scores = validation_curve(
    SVC(), X, y, param_name="gamma", param_range=gamma_candidates,
    scoring="accuracy", n_jobs=-1,cv=skf)

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
