# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:12:33 2021

@author: Neal LONG
"""
from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '17788161'
API_KEY = 'cQLWahrXbsindbL43shb2jsr'
SECRET_KEY = '0bNITwAVfIxyrVh6M9H8Mo149BtqbGcZ'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
text1 = "苹果是一家伟大的公司"
text2 = "这家公司高存高贷"
print(client.sentimentClassify(text1))
print(client.sentimentClassify(text2))