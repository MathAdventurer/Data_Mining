# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:08:42 2019

@author: Neal
"""

import requests
response = requests.get('http://httpbin.org/headers')
print(response.status_code)
print(response.text)

print("\n","="*30, "UA")
fake_header = {  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2"
        }
#send http request with fake http header
response = requests.get('http://httpbin.org/headers',headers = fake_header)
print(response.status_code)
print(response.text)

print("\n","="*30, "ERROR")
#Handle error response
response = requests.get('http://httpbin.org/haha',headers = fake_header)
print(response.status_code)
print(response.text)

print("\n","="*30, "Session Cookie")
# session can persist cookie 
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'


print("\n","="*30, "Failed Cookie")
# request CANNOT persist cookie 

requests.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = requests.get('https://httpbin.org/cookies')

print(r.text)
# '{"cookies": {}}'



