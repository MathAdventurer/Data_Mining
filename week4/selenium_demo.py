#coding=utf8
"""
Created on Sat Mar 14 18:30:07 2020

@author: Neal LONG
https://selenium-python.readthedocs.io/

1. pip install selenium
2. Download the driver https://github.com/mozilla/geckodriver/releases (if Firefox)
"""

from selenium import webdriver
print(dir(webdriver))
# 初始化测试器
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# 更多功能, print(dir(driver)) 接入正则表达式
# print([i for i in dir(driver) if "__" not in i])
driver.get("https://www.xueqiu.com/")
print(driver.title)
# 关闭测试器
driver.close()


