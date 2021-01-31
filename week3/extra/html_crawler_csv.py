# -*- coding: utf-8 -*-
"""
Created on Feb 25 11:05:46 2020

@author: Neal
"""

import requests
from bs4 import BeautifulSoup
import csv
import time #***

fake_header = {  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2"
        }
#send http request with fake http header
stocks = ['000001','000002','00004','000005']

base_url = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllMemordDetail.php?stockid={:>06}'
#open file to with written permission 
with open('./data/stock_announcement_clean.csv','w',newline='',encoding='utf-8-sig') as wf:
    writer = csv.DictWriter(wf,fieldnames=("股票代码","公告日期","公告标题")) #***
    writer.writeheader()
    for stock in stocks:#process stock one by one
        #prepare the request webpage with desired parameters
        url = base_url.format(stock)
        print("Now we are crawling",stock)
        response = requests.get(url,headers = fake_header)
        if response.status_code == 200:
            response.encoding = 'gb2312'#because sina use 
            root = BeautifulSoup(response.text,"html.parser") 
            # search all the announcement tag by tag name and attribute/values
            title_divs = root.find_all('div',attrs={'class':'title_cls'})
            for div in title_divs:#get and store announcement title one by one  
                date_str="Missing"
                for sibling in div.next_siblings:
                    if sibling.name=='center':
                        date_str= sibling.get_text().strip()[5:]
                        break
                title = div.get_text().strip()[6:]#***
                writer.writerow({"股票代码":stock,"公告日期":date_str,"公告标题":title} )  #***
        else: 
            print("Faisled to crawl", stock)
        time.sleep(1)  #***sleep 1 second
                