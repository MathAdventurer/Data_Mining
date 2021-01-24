#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Wang,Xudong 220041020 SDS time:2021/1/24


# 1. Exercise on String

def calculate_len_string(string: str):
    num = 0
    for _ in string:   # if the variable is not used , it's better changed to _.
        num += 1
    return num


"""
2. Values-type casting

bool() use to do the data type casting, only empty string will return the False

bool(0) and bool("") and bool(None) are False

all number except 0 will return the Ture 


3. Math Operations (in math module)

log(...)
    log(x, [base=math.e])
    Return the logarithm of x to the given base.    
    If the base not specified, returns the natural logarithm (base e) of x.
log10(x, /)
    Return the base 10 logarithm of x.

"""


if __name__ == "__main__":
    calculate_len_string("apple")
