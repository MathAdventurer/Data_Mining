# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:28:21 2021

@author: Neal LONG
"""


import pandas as pd

df = pd.read_pickle("./data/sz000001_2020.pkl")

#++insert your code here++
#Q2-1
# Using pandas unique method to ensure there's no repeated day.
print("The number of trading days among the first 100 rows of dataframe df\
having 'open' price lower than 'close' price is", \
      len(df[:100][df[:100]["open"]<df[:100]["close"]]["trade_date"].unique()))
#Q2-2
print('The average \'high\' price for all trading days in df \
with \'open\' price lower than \'close\' is {:.2f}'\
      .format(df[df["open"]<df["close"]]["high"].mean()))