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

# 4. Mutable Vs. Immutable

import ctypes

value = 'hello world'  # 定义一个字符串变量
address = id(value)  # 获取value的地址，赋给address
get_value = ctypes.cast(address, ctypes.py_object).value  # 读取地址中的变量
print(get_value)

a = 1
print(id(a))
add_1 = id(a)
a = a+1
print(id(a))
get_value = ctypes.cast(add_1, ctypes.py_object).value
print(get_value)
b = 1
print(id(b))
c = 1
print(id(c))
d = a
v,n,m = 1,1,1

print(id(v),id(n),id(m),id(d))
"""
以上的结果输出： 
hello world
4562020704
4562020736
1
4562020704
4562020704
4562020704 4562020704 4562020704 4562020736

python的数据类型中，Immutable的每个值都对应一个自己的内存地址，且相等的值都是指向相同的地址

"""
a = {1,2,4,5,6,7}
print(id(a))
a.add((111,2323))
print(id(a))
a.add('hhhhhhhhhhhh')
print(id(a))
a.add(5.6)
print(id(a))
a.add(8)
print(id(a))
for i in range(100,1000000):
    a.add(i)
print(id(a))

if __name__ == "__main__":
    calculate_len_string("apple")
