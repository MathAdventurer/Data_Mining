#coding=utf8
"""
Created on Tue Jan 19 23:55:41 2021

@author: Neal LONG
"""
# 类的definition  instance实例化  .attri .method

class Person:
    
    def __init__(self, name, birth_year=1998):
        self.birth_year = birth_year
        self.name = name
        self.age =  2021 - self.birth_year
            
    def update_age(self, year):
        self.age =  year - self.birth_year
        
    def print_age(self):
        print("Age of", self.name, "is", self.age)  # instance attribute
        

        
if __name__ == "__main__":
    jim = Person("Jim", 1998)
    lilei = Person("Lilei",1998)
    jim.print_age()
    jim.update_age(2022)
    jim.print_age()
    print(jim.age)

    
    lilei.print_age() #?
