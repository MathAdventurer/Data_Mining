# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:23:17 2018

@author: Neal
"""

import csv
csv_data_path='./data/complex_data.csv'

with open(csv_data_path,'w',newline='',encoding='utf8') as wf:
    writer = csv.writer(wf)
    writer.writerow((1,"Hello \n World"))
    writer.writerow((2,"""This, is a "complex" \n record"""))
    writer.writerow((3,"The end"))
    
with open(csv_data_path,'r',newline='',encoding='utf8') as rf:
    reader = csv.reader(rf)
    for row in reader:
        print(row)