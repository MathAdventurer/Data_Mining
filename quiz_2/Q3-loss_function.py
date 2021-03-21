#coding=utf8
"""
Created on Thu Mar 12 17:48:23 2020

@author: Neal LONG

Hint max() is a built-in function in Python 
"""
import pickle
import math
import numpy as np

def linear_func(W,X):
    """
    General form of a 2-d linear function with w0 as intercept
    W = [w0,w1,w2], X = [x1,x2]
    f_x = w0 + w1 * x1 + w2 * x2
    """
    # pass #++insert your code here ++ to replace pass++
    linear_func_output = W[0]+np.dot(X,W[1:].reshape(W[1:].shape[0],1))
    return linear_func_output

def hinge_loss(f_x,y_true):
    """
    Compute the hinge loss given the returned value f_x from
        a linear discrimination function on the feature x and its label y
    """
    # pass #++insert your code here ++ to replace pass++
    loss_vector = np.ones_like(f_x * y_true) - f_x * y_true
    loss_vector[loss_vector <= 0] = 0
    return loss_vector.sum()

def logistic_loss(f_x,y_true):
    """
    Compute the logistic_loss loss given the returned value f_x from
    a linear discrimination function on the feature x and its label y.
    Please use logarithm with base = 2
    """
    # pass #++insert your code here ++ to replace pass++
    loss_vector = np.ones_like(f_x) + math.e ** (-y_true * f_x)
    loss_vector = np.array([math.log2(x) for x in loss_vector])
    loss_vector = loss_vector.reshape(loss_vector.shape[0], 1)
    return loss_vector.sum()

def zero_one_loss(f_x,y_true):
    """
    Compute the zero-one loss given the returned value f_x from
        a linear discrimination function on the feature x and its label y
    """
    # if f_x*y_true>=0:
    #     return 0
    # else:
    #     return 1
    loss_vector = np.ones_like(f_x)
    loss_vector[loss_vector*y_true >= 0] = 0
    return loss_vector.sum()
    
with open('./data/Q3_fetures.pkl','rb') as rf:
    X = pickle.load(rf)

with open('./data/Q3_labels.pkl','rb') as rf:
    Y_true = pickle.load(rf)

Y_true = Y_true.reshape(Y_true.shape[0],1)
print(len(X),len(Y_true))
    
W = np.array([-0.45236953,2.23604794, -3.94803128])

x_i = X[6]
f_x_i=linear_func(W,x_i)
y_i = Y_true[6]
loss = zero_one_loss(f_x_i,y_i)

print('zero-one error in 7-th case with f_x={} ,and y={}:'.format(linear_func(W,x_i),y_i))

W1 = np.array([-0.75862686,1.50126098,-2.3948365])
W2 = np.array([-0.67862686,1.50126098,-2.3948365])
W3 = np.array([-0.59862686,1.50126098,-2.3948365])


# Solution

Y_true = Y_true.reshape(Y_true.shape[0],1)
#Compute total zero_one_loss for all training data and compare 
#++insert your code here++
W_list  = [W1,W2,W3]
print("For the total zero_one_loss:")
i = 0
for W in W_list:
    Y_Pred = linear_func(W, X)
    loss = zero_one_loss(Y_Pred, Y_true)
    print(f"The total zero_one loss for W{i+1} is {loss}")
    i+=1
print("\n")
#Compute total hinge loss for all training data and compare 
#++insert your code here++
print("For the hinge_loss:")
i = 0
for W in W_list:
    Y_Pred = linear_func(W, X)
    loss = hinge_loss(Y_Pred, Y_true)
    print(f"The total hinge_loss for W{i+1} is {loss}")
    i += 1
print("\n")
#Compute total logistic loss for all training data and compare 
#++insert your code here++

print("For total logistic_loss:")
i = 0
for W in W_list:
    Y_Pred = linear_func(W, X)
    loss = logistic_loss(Y_Pred, Y_true)
    print(f"The total logistic_loss for W{i+1} is {loss}")
    i += 1
print("\n")