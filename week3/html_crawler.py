# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 11:05:46 2019

@author: Neal
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

fake_header = {  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2"
        }
#send http request with fake http header
stocks = ['000001','000002','000004','000005']

base_url = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllMemordDetail.php?stockid='
#open file to with written permission 
results = []
for stock in stocks:#process stock one by one
    #prepare the request webpage with desired parameters
    url = base_url+stock
    print("Now we are crawling stock",url)
    response = requests.get(url,headers = fake_header)
    if response.status_code == 200:
        response.encoding = 'gb2312'#because sina use 
        html = BeautifulSoup(response.text,"html.parser") 
        # search all the announcement tag by tag name and attribute/values
        title_divs = html.find_all('div',attrs={'class':'title_cls'})
        for div in title_divs:#get and store announcement title one by one  
#                writer.writerow([stock,div.get_text().strip()])
            date_str="Missing"
            for sibling in div.next_siblings:
                if sibling.name=='center':
                    date_str= sibling.get_text().strip()
                    break
            results.append([stock,date_str,div.get_text().strip()] ) 
                
                
print(results)

new_df = pd.DataFrame(columns=['Stock', 'Date','Title'], data=results)
new_df.to_excel("./data/web_crawl_results.xlsx")