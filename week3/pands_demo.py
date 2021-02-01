# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:17:15 2020

@author: Neal LONG
"""

import pandas as pd
import pickle


df = pd.read_csv('./data/wanke_data.csv')
print("Successfully read the file")
with open("./data/wanke_data.pkl","wb") as wf:
    pickle.dump(df,wf)
print("Successfully save the df in pickle")
del df
print("reload the df from the file")
df = pd.read_pickle('./data/wanke_data.pkl')
print(df.head())
print('='*40) # 语法糖，分割线
print(df.describe()) # 统计描述
print('='*40)
print(df.info()) # 行列信息，数据类型
print('='*40)
print(df.index) # 索引的信息
print('='*40)
print('='*40)
low2high=df[df['Open']<df['Close']][['Open','Close']] # 索引并选取
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

df['Open']=df['Open'].apply(minus5) # 使用apply方法
print(f"df['Open'].mean()={df['Open'].mean()}")
print('='*40)
print('='*40)
df['l2h'] = df['Open']<df['Close']
print(df.head())
print('='*40)
print(df.groupby('l2h')['Volume'].mean())



