# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:21:46 2018

@author: Neal
"""

import json
data_path = './data/dict.json'

# A simple dict is supported by json.
data = {
    'a': [1, 2.0, 3],
    'b': ("character string", "byte string"),
    'c': [None, True, False]
}

print("==Data dumped to JSON file ==")
print(data)
with open(data_path, 'w') as wf: 
    # Pickle the 'data' dictionary
    json.dump(data, wf) 
    
print("\n==Data loaded from JSON file ==")    
with open(data_path, 'r') as rf:
    # Load the 'data' dictionary back from json
    data_new = json.load(rf)  
print(data_new)