
#coding=utf8
"""
Created on Thu Mar 19 00:14:26 2020

@author: Neal LONG


Advantages of GridSearchCV:
    0. Less code
    1. Concurrent execution with n_jobs >1
    2. Detailed information during selection
    3. Retrained model on all training data

"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV


# Load data
iris = load_iris()

# Determine feature matrix X and taget array Y
X = iris.data[:,:2]
y = iris.target
candidate_max_depth = [1,2,3,4,5,6]


parameters = {'max_depth':  candidate_max_depth}
basic_clf = DecisionTreeClassifier(random_state=0)
gcv_clf = GridSearchCV(basic_clf, parameters,cv=5,n_jobs=-1,iid=False,
                   scoring='accuracy')
gcv_clf.fit(X, y)
print("Based on GridSearchCV, the best max_depth is {}".format(
        gcv_clf.best_params_['max_depth']))

plt.figure(1, figsize=(8, 8))
plt.ylabel("Accuracy")
plt.xlabel("max_depth")
plt.plot(candidate_max_depth, gcv_clf.cv_results_['mean_test_score'],'o-',
         label = "Mean Acc. from 5-fold CV")
plt.grid(True)
plt.legend()    
plt.title('Choose best max_depth with 5-fold test') 
plt.show()















