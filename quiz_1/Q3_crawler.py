# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:02:26 2017

@author: Neal
shareholder information of a stock are listed in :
https://q.stock.sohu.com/cn/000001/ltgd.shtml
https://q.stock.sohu.com/cn/000002/ltgd.shtml
https://q.stock.sohu.com/cn/000003/ltgd.shtml
...

"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
fake_header = {  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2"
        }

data_file= './data/stock_shareholders.csv'
sz50_stocks=('600000','601988','601985','601901','600111','601857','601818',
             '601800','601788','601766','601688','601668','601628','601601',
             '601398','601390','601336','601328','601318','601288','601229',
             '601211','601198','601186','601169','601166','601088','601006',
             '600999','600958','600919','600887','600837','600606','600547',
             '600519','600518','600485','600340','601881','600104','600100',
             '600050','600048','600036','600030','600029','600028','600016',
             '601989')

sz50_top10_stocks = sz50_stocks[:10]

print('There are',len(sz50_top10_stocks), 'stocks in sz50_top10_stocks')

base_url = 'https://q.stock.sohu.com/cn/{}/ltgd.shtml' 
row_count = 0
#create a list to store the crawled share-holdoing records
results=[]
for stock in sz50_top10_stocks:#process stock one by one
    #prepare the request webpage with desired parameters
    url = base_url.format(stock)
    print("Now we are crawling stock",stock)
    #send http request with fake http header
    response = requests.get(url,headers = fake_header)
    if response.status_code == 200:
        response.encoding = 'gb2312' # ++insert your code here++
        root = BeautifulSoup(response.text,"html.parser") 
        # search the table storing the shareholder information
        # ++insert your code here++
        table = root.find_all('table',attrs={"class":"tableG"})[0]
        #print(table)
        # list all rows the table, i.e., tr tags
        rows = table.find_all('tr')
        for row in rows: #iterate rows
            record=[stock,]# define a record with stock pre-filled and then store columns of the row/record
            # list all columns of the row , i.e., td tags
            columns = row.find_all('td')
            for col in columns: #iterate colums
                record.append(col.get_text().strip())
            if len(record) == 7:# if has valid columns, save the record to list results
                #++insert your code here++
                results.append(record)
                row_count+=1
        time.sleep(1)
    print('Crawled and saved {} records of  shareholder information of sz50_top10_stocks to{}'.format(row_count,data_file))

sharehold_records_df = pd.DataFrame(columns=['stock', 'rank','holder','shares','percentage','changes','nature'], data=results)
sharehold_records_df.to_excel("./data/sharehold_records.xlsx")
sharehold_records_df = pd.read_excel("./data/sharehold_records.xlsx")
print("List of shareholers are ", sharehold_records_df['holder'])

#++insert your code here++ to count and sort the frequency/total shares of shareholers

# Change the 'percentage' datatype from string to float.
sharehold_records_df['percentage']=sharehold_records_df['percentage'].str.strip("%").astype(float)/100
# Sort the information we needed and output the answer.
shareholers_freq = sharehold_records_df['holder'].value_counts().sort_values(ascending=False)
shareholers_percentage = sharehold_records_df.groupby('holder')['percentage'].sum().sort_values(ascending=False)
print('\n')
print("="*40)
print("sort the frequency of shareholers:")
print(shareholers_freq)
print(f"The organization which holds the 4th most stocks in sz50_top10 is \
{shareholers_freq[3:4,].index[0]}, with frequency is {shareholers_freq[3:4,].values[0]}")

print('\n')
print("="*40)
print("sort the percentage of shareholers:")
print(shareholers_percentage)
print(f"The organization which holds the most total percentage of shares of stocks in sz50_top10 is \
{shareholers_percentage[0:1,].index[0]}, with percentage is {shareholers_percentage[0:1,].values[0]}")