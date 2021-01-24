# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:50:56 2020

@author: Neal
"""

import pandas as pd

csv_data_path='./data/wanke_data.csv'


wanke_csv =  pd.read_csv(csv_data_path)
print(wanke_csv.head())

# Save/load the dataframe from the pickle file
pickle_path='./data/wanke_data.pkl'
wanke_csv.to_pickle(pickle_path)
wanke_new_pickle = pd.read_pickle(pickle_path)
print("="*30)
print("Shapes of wanke_csv and wanke_pickle are the same?",wanke_csv.shape == wanke_new_pickle.shape)
print(wanke_new_pickle.head())

# Save/load the dataframe from the above excel file
excel_path='./data/wanke_data.xlsx'
wanke_csv.to_excel(excel_path,index=False)
wanke_new_excel = pd.read_excel(excel_path)
print("="*30)
print("Shapes of wanke_csv and wanke_excel are the same?",wanke_csv.shape == wanke_new_excel.shape)
print(wanke_new_excel.head())
    

# Save/load the dataframe from the above html file
html_path='./data/wanke_data.html'
wanke_csv.to_html(html_path,index=False)
wanke_new_html = pd.read_html(html_path)[0]
print("="*30)
print("Shapes of wanke_csv and wanke_html are the same?",wanke_csv.shape == wanke_new_html.shape)
print(wanke_new_html.head())