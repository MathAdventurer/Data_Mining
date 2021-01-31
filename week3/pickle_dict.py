# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:21:46 2020

@author: Neal
"""

import pickle
data_path = './data/dict.pkl'

# An arbitrary collection of objects supported by pickle.
data = {
    'a': [1, 2.0, 3],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

print("==Data dumped to pickle==")
print(data)
with open(data_path, 'wb') as wf: 
    # Pickle the 'data' dictionary
    pickle.dump(data, wf) 
    
with open(data_path, 'rb') as rf:
    # Load the 'data' dictionary back from pickle
    data_new = pickle.load(rf)  
print("\n==Data loaded from pickle==")
print(data_new)