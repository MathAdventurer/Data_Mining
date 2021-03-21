# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:31:39 2020

@author: Neal LONG
"""

from sklearn.model_selection import StratifiedKFold,KFold

#from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np

X = np.arange(32).reshape((16, 2))
y = np.array( [0]*8+[1]*8)

#################

print("="*30)
print("="*5,'Random shuffle split CV',"="*5)
print("="*30)

for i in range(4):  
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                        test_size=0.25,random_state=i)
    print(i,"-"*30)
    print('X_train=\n', X_train)
    print("y_train = ", y_train)
    print('X_test=\n', X_test)
    print("y_test = ", y_test)

#################
     
print("="*30)
print("="*5,'KFold CV',"="*5)
print("="*30)     

kf = KFold(n_splits=4)
i=0
for train_index, test_index in kf.split(X, y):
     X_train, X_test = X[train_index], X[test_index]
     y_train, y_test = y[train_index], y[test_index]
     print(i,"-"*30)
     print('X_train=\n', X_train)
     print("y_train = ", y_train)
     print('X_test=\n', X_test)
     print("y_test = ", y_test)
     i+=1
 
#################

print("="*30)
print("="*5,'Stratified random shuffle split CV',"="*5)
print("="*30)

for i in range(4):  
    X_train, X_test, y_train, y_test = train_test_split(X, y,stratify=y, 
                                        test_size=0.25,random_state=i)
    print(i,"-"*30)
    print('X_train=\n', X_train)
    print("y_train = ", y_train)
    print('X_test=\n', X_test)
    print("y_test = ", y_test)

    
#################    
     
print("="*30)
print("="*5,'StratifiedKFold CV',"="*5)
print("="*30)

skf = StratifiedKFold(n_splits=4)
i=0
for train_index, test_index in skf.split(X, y):
     X_train, X_test = X[train_index], X[test_index]
     y_train, y_test = y[train_index], y[test_index]
     print(i,"-"*30)
     print('X_train=\n', X_train)
     print("y_train = ", y_train)
     print('X_test=\n', X_test)
     print("y_test = ", y_test)
     i+=1     
     