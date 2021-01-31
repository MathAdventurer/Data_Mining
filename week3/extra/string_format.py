# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:23:07 2020

@author: Neal LONG

Try to construct URL with string.format
"""

base_url = "http://quotes.money.163.com/service/gszl_{:>06}.html?type={}"
stock = "000002"
api_type = 'cp'

print("http://quotes.money.163.com/service/gszl_"+stock+".html?type="+api_type)
print(base_url.format(stock,api_type))

print('='*40)
stock = "00002"

print("http://quotes.money.163.com/service/gszl_"+stock+".html?type="+api_type)
print(base_url.format(stock,api_type))
      
print('='*40)
print('='*40)      
print('{:>6}'.format('236'))
print('{:>06}'.format('236'))


print('{:>6}'.format('236'))
print('{:>6}'.format('236'))
print('{:>06}'.format('236'))

print("Every {} should know the use of {} {} programming and {}"
    .format("programmer", "Open", "Source", "Operating Systems")) 
  

print("Every {3} should know the use of {2} {1} programming and {0}"
        .format("programmer", "Open", "Source", "Operating Systems")) 