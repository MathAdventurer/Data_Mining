# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:17:15 2020

@author: Neal LONG
"""

import pandas as pd


df = pd.read_pickle('./data/wanke_data.pkl')
print(df.head())
print('='*40)
print(df.describe())
print('='*40)
print(df.info())
print('='*40)
print(df.index)
print('='*40)
print('='*40)
low2high=df[df['Open']<df['Close']][['Open','Close']]
print(low2high.head())
print(low2high.shape)
print(len(low2high))
print("df['Open'].mean()=",df['Open'].mean())
print(f"df['Open'].std()={df['Open'].std()}")
print('='*40)
df['Open']+=5
print(f"df['Open'].mean()={df['Open'].mean()}")

print('='*40)

def minus5(x):
    return x-5

df['Open']=df['Open'].apply(minus5)
print(f"df['Open'].mean()={df['Open'].mean()}")
print('='*40)
print('='*40)
df['l2h'] = df['Open']<df['Close']
print(df.head())
print('='*40)
print(df.groupby('l2h')['Volume'].mean())



