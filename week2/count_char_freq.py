#coding=utf8
"""
Created on Mon Sep 11 23:13:40 2018

@author: Neal LONG

char_freq={'a':3,'b':4,}
"""

long_str= 'abcbdbabdbabbbbdsbbcbdbsbabdbcbsbd'
char_freq=dict()

for char in long_str:
    if char not in  char_freq: #first occurrence
        # write your code here #
        pass
    else:  # already exists
        # write your code here #
        pass
print("Iterate keys")
for char in char_freq:
    print(char)
print("Iterate (key,value) pairs")
for char,freq in char_freq.items():
    print(char,'appears',freq,'times in long_str')
    

