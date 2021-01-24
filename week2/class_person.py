#coding=utf8
"""
Created on Tue Jan 19 23:55:41 2021

@author: Neal LONG
"""

class Person:
    
    def __init__(self,birth_year,name):
        self.birth_year = birth_year
        self.name = name
        self.age =  2021 - self.birth_year
            
    def update_age(self, year):
        self.age =  year - self.birth_year
        
    def print_age(self):
        print("Age of", self.name, "is", self.age)
        
if __name__ == "__main__":
    neal = Person(1998,"Neal")
    neal.print_age()
    neal.update_age(2022)
    neal.print_age()
    