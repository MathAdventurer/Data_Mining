#coding=utf8
"""
Created on Thu Sep  5 11:02:00 2019

@author: Neal LONG

https://tushare.pro/document/2?doc_id=27
"""

import tushare as ts



#（your token可以在免费注册后，个人主页的“接口Token”下找到）
api = ts.pro_api("128c6908532bde66c7594f02b66e210139c2ce2c175484358d477c30")

result = api.daily(ts_code='000001.SZ', start_date='20200214', end_date='20200220')
result.to_excel('./data/sz000001.xlsx')