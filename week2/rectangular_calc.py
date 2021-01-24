#coding=utf8
"""
Created on Thu Sep 01 18:04:16 2019

@author: Neal LONG
"""

def calc_rect(height,a=1,b=2,width=5,*args,**kwargs): # 从第五个开始匹配进入 *arg
    perimeter = 2*(height+width)
    area = height*width
    print(*args)
    print(**kwargs)
    print(area)
    return perimeter, area

# print(calc_rect(2))
width = input("Please input width:")
height = input("Please input height:")
p,a = calc_rect(int(height),int(width))
print("The perimeter is",p, "and area is",a)
print(calc_rect(4,3))
print(calc_rect(4,3))
calc_rect(4,3,3,4,5,m=14)

