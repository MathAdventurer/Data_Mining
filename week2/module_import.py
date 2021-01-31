# coding=utf8
"""
Created on Tue Jan 19 23:06:42 2021

@author: Neal LONG
"""
import sys
import imp
MyModule = imp.load_source('MyModule', "/Users/mac/Desktop/MDS5724_DataMining/Data_Mining_Codes/Data_Mining/week2/MyModule.py")
import MyModule as mm
person_name = "Jim"

# from MyModule import person_name


mm.greeting(person_name)
print(mm.pi*(10**2))
