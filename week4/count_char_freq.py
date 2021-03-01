#coding=utf8
"""
Created on Mon Feb 8 23:13:40 2021

@author: Neal LONG
"""


#  count the frequency of letter appeared in the string
long_str= 'abcbdbabdbabbbbdsbbcbdbsbabdbcbsbd'
char_freq= dict()

for char in long_str:
    if char not in  char_freq: #first occurrence
        char_freq[char] = 1 #insert your code here #
    else:  # already exists
        char_freq[char] += 1#insert your code here #
print("Iterate keys")
for ch in char_freq:
    print(ch)
print("Iterate (key,value) pairs")
# 格式化输出
for ch,freq in char_freq.items():
    print(ch,'appears',freq,'times in long_str')
print("===before sorting=======")

# sort the frequency
char_freq_sorted = sorted(char_freq.items(), key=lambda x:x[1], reverse=True)
# dict.item 返回的是一个元组的形式，使用lambda函数进行转换，reverse是降序排列
# sorted 返回的是一个 list object

# [('b', 18), ('d', 6), ('a', 4), ('c', 3), ('s', 3)]

# 关于sorted 函数的用法
#the built-in function **sorted** that takes a sequence as parameter and returns a sorted sequence.
# Help on built-in function sorted in module builtins:
# sorted(iterable, /, *, key=None, reverse=False)
#     Return a new list containing all items from the iterable in ascending order.
#
#     A custom key function can be supplied to customize the sort order, and the
#     reverse flag can be set to request the result in descending order.

print("The most frequent character is", char_freq_sorted[0][0])

print("===after sorting=======")    

for ch,freq in char_freq_sorted:
    print(ch,'appears',freq,'times in long_str')




# Python  dict to reverse the dict and sorted

# The return value for dict items() method is the tuple with (key,value), the length is 2.
# python 语法糖对元组分别赋值 x,y = (1,2)

#type((1,2))
# Out[18]: tuple
# type({1,2,4,5})
# Out[19]: set

c = {'a':10, 'c': 22, 'b':5}
tmp = list()
for k, v in c.items():
    tmp.append((v,k))
print(tmp)

tmp = sorted(tmp)
print(tmp)

tmp = sorted(tmp, reverse = True)
print(tmp)
tmp = dict(tmp)
print(tmp)

# reverse the dictionary

tmp = dict()
for key,value in char_freq.items():
    tmp[value] = key
print(tmp)
print(sorted(tmp,reverse=True))
tmp_1 = dict()
for i in sorted(tmp,reverse=True):
    print(tmp[i],i)
    tmp_1[tmp[i]] = i
print(tmp_1)


