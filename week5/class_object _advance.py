# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:51:04 2020

@author: Neal LONG
"""

class Person:
    class_attr = "person" #新用法，适用于全class attributes,不实例化也可以使用
    
    def __init__(self, input_name="haha", input_age=22):
        self.name = input_name
        self.age = input_age

    def myfunc(self):
        print("Hello my name is " + self.name)
        
    def class_func():
        print("Hello World")

p1 = Person("John", 36)
p1.myfunc()
print(Person.class_attr)
print(Person().class_attr)
Person.class_func()
# No Person.myfunc()
# No Person.name
# No p1.class_func()