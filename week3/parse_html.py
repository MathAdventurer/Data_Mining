#coding=utf8
"""
Created on Wed Sep 20 23:10:43 2018

@author: Neal LONG
"""

import pandas as pd
from bs4 import BeautifulSoup

#Read HTML string from file
with open('./data/table.html','r',encoding='utf8') as rf:
    html_string = rf.read()
    
print(html_string)
print("\n", "="*30, "\n")
# Parse the HTML string and get the root of DOM
root = BeautifulSoup(html_string,"html.parser") 

table = root.find('table',attrs={'id':2}) # Locate the table under the 
print(table)
print("\n", "="*30, "\n")
# I know the size of table is 2 rows * 3 columns
desire = None
row_marker = 1
#get the children rows under table
for row in table.find_all('tr'):
    column_marker = 1
    #get the children columns under row tr
    columns = row.find_all('td')
    for column in columns:
        if row_marker == 2 and column_marker ==2:
        desire = column.get_text()
        print("We are now proceesing row=",row_marker,"and column=",column_marker,' with value=',column.get_text())
        column_marker += 1 #process next column of current row
    row_marker+=1 #process next row

