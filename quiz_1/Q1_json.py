# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 23:01:16 2021

@author: Neal LONG

"""

import json

with open('./data/SZ000063.json',encoding='utf8') as rf:
    xueqiu_json = json.load(rf)

#Q1-0 
#++insert your code here++
print("The number of posts in JSON is",len(xueqiu_json['list']))

# Fetch the id of 2nd post
print("The id of second post is", xueqiu_json['list'][1]['id'])

#++insert your code here++
# Q1-1
# How many posts in total with its 'text'  attribute containing the word "5G"?

# Using python list syntactic sugar solve and answer this question just for a single print command lines.
print("The number with its 'text' attribute containing the word \"5G\" is ",\
      len([xueqiu_json['list'][i]['text'] for i in range(len(xueqiu_json['list'])) if "5G" in xueqiu_json['list'][i]['text']]))
