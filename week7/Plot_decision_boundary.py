#coding=utf8
"""
Created on Thu Mar 12 17:48:23 2020

@author: Neal LONG

Hint max() is a built-in function in Python 
"""

import pickle
import matplotlib.pyplot as plt
import numpy as np


def hinge_loss(f_x,y_true,margin=1):
    """
    Compute the hinge loss given the returned value from 
        a linear discrimination function on the feature x and its label y 
    """
    return max(0,margin-y_true*f_x)
#    pass #++insert your code here to replace pass++
    

def zero_one_loss(f_x,y_true):
    """
    Compute the zero-one loss given the returned value from 
        a linear discrimination function on the feature x and its label y
    """
    if f_x*y_true>=0:
        return 0
    else:
        return 1
    
with open('Q2_fetures.pkl','rb') as rf:
    X = pickle.load(rf)

with open('Q2_labels.pkl','rb') as rf:
    Y_true = pickle.load(rf)

Y_true[Y_true==0]=-1



print(len(X),len(Y_true))

def linear_func(W,X):
    """
    General form of a 2-d linear function with w0 as intercept
    """
    return W[0]+W[1]*X[0]+W[2]*X[1]

def boundary_line(W,x):
    y= -(W[0]+W[1]*x)/W[2]
    return y
    
W = (-0.45236953,2.23604794, -3.94803128)
#f(x) = -0.45236953+2.23604794*X[0]-3.94803128*X[1] = 0
#        ->3.94803128*X[1] = -0.45236953+2.23604794*X[0]
#           y = (-0.45236953+2.23604794*x)/3.94803128

plt.figure(1, figsize=(8, 8))
plt.scatter(X[:, 0], X[:, 1], c=Y_true)

 #generate dense plots
s = np.arange(min(X[:, 0]),max(X[:, 0]),0.1)

#generate the corresponding y for each z in s
t = []
for z in s:
    t.append((-0.45236953+2.23604794*z)/3.94803128)
    
    
#plt.plot(s, t,label = 'W')

#
W1 = (-0.762686,1.50126098,-2.3948365 )
W2 = (-0.422686,1.50126098,-2.3948365 )
W3 = (-0.59862686,1.50126098,-2.3948365)

# W1 = (-0.5986268-1,1.50126098,-2.3948365 )
# W2 = (-0.5986268+1,1.50126098,-2.3948365 ) 
# W3 = (-0.59862686,1.50126098,-2.3948365 )

W1 = (-0.59862686-0.17,1.50126098,-2.3948365 ) 
W2 = (-0.59862686+0.17,1.50126098,-2.3948365 ) 
W3 = (-0.59862686,1.50126098,-2.3948365 )




for W, label in zip((W1,W2,W3), ('W1','W2','W3')):
    #zip((W1,W2,W3), ('W1','W2','W3')) = [(W1,'W1',1),(W2,'w2',2),(W3,'W3',3)]
    t = [boundary_line(W, x) for x in s]
    plt.plot(s, t, label = label)

plt.legend()    
plt.show()



# #class zip(object)
#  |  zip(*iterables) --> zip object
#  |
#  |  Return a zip object whose .__next__() method returns a tuple where
#  |  the i-th element comes from the i-th iterable argument.  The .__next__()
#  |  method continues until the shortest iterable in the argument sequence
#  |  is exhausted and then it raises StopIteration.

# 对应相同维度的数据
# zip.__next__() 相当于 next(), iteration结束后都会报错
#Compute zero_one_loss
print("\nZero one loss:")
for W, label in zip((W1,W2,W3), ('W1','W2','W3')):  # 对应赋值, zip 函数
    zero_one_loss_total = 0
    for i in range(len(X)):
        x_i = X[i]
        f_x_i=linear_func(W,x_i)
        y_i = Y_true[i]
        loss = zero_one_loss(f_x_i,y_i)
        if loss >0:
#            print(i,f_x_i,y_i,loss)
            zero_one_loss_total+=loss   
    print(label, zero_one_loss_total)

#Compute hinge loss
print("\nHinge loss:")   
for W, label in zip((W1,W2,W3), ('W1','W2','W3')):
    hinge_loss_total = 0
    for i in range(len(X)):
        x_i = X[i]
        f_x_i=linear_func(W,x_i)
        y_i = Y_true[i]
        loss = hinge_loss(f_x_i,y_i,1)
        if loss >0:
            hinge_loss_total+=loss   
    print(label, hinge_loss_total)


