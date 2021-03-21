#coding=utf8
"""
Created on Thu Mar 12 17:48:23 2020

@author: Neal LONG

Hint max() is a built-in function in Python 
"""
import pickle
import math

def linear_func(W,X):
    """
    General form of a 2-d linear function with w0 as intercept
    W = [w0,w1,w2], X = [x1,x2]
    f_x = w0 + w1 * x1 + w2 * x2
    """
    return W[0]+W[1]*X[0]+W[2]*X[1]


def hinge_loss(f_x,y_true):
    """
    Compute the hinge loss given the returned value f_x from 
        a linear discrimination function on the feature x and its label y 
    """
    return max(0,1-y_true*f_x)
#    pass #++insert your code here to replace pass++
    
def logistic_loss(f_x,y_true):
    """
    Compute the logistic_loss loss given the returned value f_x from 
    a linear discrimination function on the feature x and its label y. 
    Please use  logarithm with base = 2 
    """
    return math.log(1+math.exp(-f_x*y_true),2)
#    pass #++insert your code here to replace pass++
    


def zero_one_loss(f_x,y_true):
    """
    Compute the zero-one loss given the returned value f_x from 
        a linear discrimination function on the feature x and its label y
    """
    if f_x*y_true>=0:
        return 0
    else:
        return 1
    
with open('./data/Q3_fetures.pkl','rb') as rf:
    X = pickle.load(rf)

with open('./data/Q3_labels.pkl','rb') as rf:
    Y_true = pickle.load(rf)

print(len(X),len(Y_true))
    
W = (-0.45236953,2.23604794, -3.94803128)
zero_one_loss_total = 0

x_i = X[6]
f_x_i=linear_func(W,x_i)
y_i = Y_true[6]
loss = zero_one_loss(f_x_i,y_i)
print('zero-one error in 7-th case with f_x={} ,and y={}:'.format(linear_func(W,x_i),y_i))

W1 = (-0.75862686,1.50126098,-2.3948365 )
W2 = (-0.67862686,1.50126098,-2.3948365 )
W3 = (-0.59862686,1.50126098,-2.3948365 )



#Compute total zero_one_loss for all training data and compare 
results = []
for name, W  in zip(("W1","W2","W3"),(W1,W2,W3)):
    zero_one_loss_total = 0
    for i in range(len(X)):
        x_i = X[i]
        f_x_i=linear_func(W,x_i)
        y_i = Y_true[i]
        loss = zero_one_loss(f_x_i,y_i)
        if loss >0:
#            print(i,f_x_i,y_i,loss)
            zero_one_loss_total+=loss   
    results.append((name,zero_one_loss_total))
print("\nOrder by zero_one_loss:")
print(sorted(results,key=lambda x:x[1]))

#Compute total hinge loss for all training data and compare 
results = []
for name, W  in zip(("W1","W2","W3"),(W1,W2,W3)):
    hinge_loss_total = 0
    for i in range(len(X)):
        x_i = X[i]
        f_x_i=linear_func(W,x_i)
        y_i = Y_true[i]
        loss = hinge_loss(f_x_i,y_i)
        if loss >0:
#            print(i,f_x_i,y_i,loss)
            hinge_loss_total+=loss   
    results.append((name,hinge_loss_total))
print("\nOrder by hinge_loss_total:")
print(sorted(results,key=lambda x:x[1]))


#Compute total logistic loss for all training data and compare 
results = []
for name, W  in zip(("W1","W2","W3"),(W1,W2,W3)):
    logistic_loss_total = 0
    for i in range(len(X)):
        x_i = X[i]
        f_x_i=linear_func(W,x_i)
        y_i = Y_true[i]
        loss = logistic_loss(f_x_i,y_i)
        if loss >0:
#            print(i,f_x_i,y_i,loss)
            logistic_loss_total+=loss   
    results.append((name,logistic_loss_total))
print("\nOrder by logistic_loss_total:")
print(sorted(results,key=lambda x:x[1]))
