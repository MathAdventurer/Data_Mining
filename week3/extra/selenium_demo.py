#coding=utf8
"""
Created on Sat Mar 14 18:30:07 2020

@author: Neal LONG
https://selenium-python.readthedocs.io/

1. pip install selenium
2. Download the driver https://github.com/mozilla/geckodriver/releases (if Firefox)
"""

from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:\\Users\Neal\Downloads\geckodriver.exe')
driver.get("https://www.xueqiu.com/")
print(driver.title)
driver.close()


