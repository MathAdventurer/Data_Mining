#coding=utf8
"""
Created on Sat Jan 23 12:15:12 2021

@author: Neal LONG

for user in all_users:
    if user in black_list:
        reject
    else:
        other_checking
"""

import timeit

black_list = list(range(1000000))
print("First element in black_list=", black_list[0],
      "\nLast element black_list =", black_list[-1],
      "\nNumber of elements in black_list=", len(black_list))

black_set = set(black_list)
print("\nNumber of elements in black_set=", len(black_set))

exp_list = ( "0 in black_list"
            , "0 in black_set"
            , "999999 in black_list"
            , "999999 in black_set"
            , "-1 in black_list"
            , "-1 in black_set")
for exp in exp_list:
    print("="*10)
    print("Checking", exp)
    print("\t result =", eval(exp))
    print("\t speed =", timeit.timeit(exp, number=100,
                  setup="from __main__ import black_list, black_set"))