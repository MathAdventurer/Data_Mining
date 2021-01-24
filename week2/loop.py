#coding=utf8
"""
Created on Mon Nov 11 21:28:03 2019

@author: Neal LONG
"""
def count(s,c):
    """
    count the length of s except c
    """
    i=0
    for val in s:    
        if val == c:        
            continue
        i+=1
    return i



def find(s,c):
    """
    find the first occurance of c in s
    """
    i=0
    for val in s:    
        if val == c:        
            break    
        i+=1
    return i


print(count("striingiiiiiii",'i'))
print(count("striing",'i'))
print(count("string",'i'))
print(find("string",'i'))
print("string".find('i'))
