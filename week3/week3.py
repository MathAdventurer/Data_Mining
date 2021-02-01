#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Wang,Xudong 220041020 SDS time:2021/1/31

# week 3-Data I/O and Collection notes
"""
1. Data Storage:
Structured data can be stored in various data structure in memory

 Python list, tuple, set, dictionary ...
 Pandas dataframe, Numpy ndarray ...

 How to store these data persistently and share

 Python to python: pickle
 Database: SQLite, MySQL, Oracle, MS SQL, Hbase, MangoDB ...
 Data Interchange format: txt, csv, tsv, XML(/html), json, xls/xlsx (Excel), dta(STATA), ...

Structured data can be stored in various data structure in memory
 Python list, tuple, set, dictionary ...
 Pandas dataframe, Numpy ndarray ...

 How to store these data persistently and share
 Python to python: pickle
 Database: SQLite, MySQL, Oracle, MS SQL, Hbase, MangoDB ...
 Data Interchange format: txt, csv, tsv, XML(/html), json, xls/xlsx (Excel), dta(STATA), ...

2.
Types of Data – Structure

a.  Structured data refers to any data that resides in a fixed field within a record.
 Stored in tables with columns and rows: relational databases, spreadsheets, Pandas
dataframe...
 Most favorable for analysis

b.  Semi-structured data does not conform with table forms , but contains tags or other markers to separate
semantic elements and enforce hierarchies of records and fields within the data.
 Json, XML,HTML ...

c.  Unstructured data does not have a pre-defined data model or is not organized
in a pre-defined manner
 80% or even higher of data is Unstructured data : text, image, video, voice ...

3.
Types of Data – Structure (Example)

 Structured data: CSV, database, Pandas dataframe
  http://quotes.money.163.com/f10/zycwzb_600795.html#01c01

 Semi-structured data: Json, XML, HTML, XBRL ... (In data collection)
 http://api.money.126.net/data/feed/0000001,0600795,money.api?callback=_ntes_quot
e_callback5959502
 https://www.xbrl-cn.org/xbrl/yingyong/

 Unstructured data: txt, jpg, mp4
 http://quotes.money.163.com/f10/ggmx_600795_5188199.html


 4. File I/O in Python


"""


# 关于文件读写
import os
import csv
print(os.getcwd())

# 1. open write函数的用法
cwd = os.getcwd()
print(os.listdir(cwd))
f = open("./data/testIO.txt", "r+") # w+覆盖写入 ，a+ 追加写入
f.write("hello world! using the r+ 1th time.") # 必须写入字符串的格式, 写入的内容没有前面的引号
print(f.read(),"test the print")
f.close()
"""
原因 w arguments 没有写的权限
Traceback (most recent call last):
  File "/Users/mac/Desktop/MDS5724_DataMining/Data_Mining_Codes/Data_Mining/week3/week3.py", line 72, in <module>
    f = open(cwd+"testfileI/O.txt", "w")
FileNotFoundError: [Errno 2] No such file or directory: 
'/Users/mac/Desktop/MDS5724_DataMining/Data_Mining_Codes/Data_Mining/week3testfileI/O.txt'


补充：

在open方法的后面有一个‘w’，w决定了打开文件的模式为：写入
r：以只读方式打开文件；
r+：打开文件用于读写，指针位于文件的开头；
w+：打开文件用于读写，如果文件存在则打开文件，将原有内容删除；文件不存在则创建文件；
a：打开文件用于追加，指针放在文件末尾，新写入的内容会接在已有内容后面；
a+:打开一个文件用于读写，如果文件存在，则追加模式；文件不存在，新建文件，用于读写；

"""
if os.path.exists("testpy.py"):
    os.remove('testpy.py')
    print("file"+"testpy.py"+"deleted!")
else:
    print("file: "+"testpy.py"+" not existed"+os.getcwd())

with open("./data/teatIO2.txt","w+") as f:
    f.write("This line was written by with open method.")
    print(f.read())



# 2. 关于文件的读取
"""
Read Text File in Python
 read() : Reads the entire file in form of a string.
 readlines(): This reads all lines from the file object and returns them as a list 
 readline() : Reads one line of the file and returns in form of a string.
"""
with open("./data/wanke_data.csv","r") as reader:
    print(reader.read())
with open("./data/wanke_data.csv", "r") as reader:
    for line in reader:
        print(line, end = " ")
with open("./data/wanke_data.csv", "r") as reader:
    print(reader.readlines())
    print(reader.readline())


"""
Memory is usually much smaller than disk
 Processing data in small batches (row by row) is favorable
"""
# Pickle 部分

import pickle
data = "./data/wanke_data.csv"
dt = csv.DictReader(data)

print("==data dumped to pickle==")
print(dt)

if os.path.exists("./data/test.pkl"):
    os.remove('test.pkl')
    print("file"+"test.pkl"+"deleted!")
else:
    print("file: "+"test.pkl"+" not existed"+os.getcwd())

with open("./data/teatIO2.txt","w+") as f:
    f.write("This line was written by with open method.")
    print(f.read())

with open("./data/test.pkl","wb") as wf:
    pickle.dump(dt,wf)
with open("./data/test.pkl","rb") as rf:
    data_new = pickle.load(rf)
print("\n==Data loaded from pickle==")
print(data_new)


with open("./week3/data/testwrite.txt","w+") as f:
    a = [str(i) for i in range(100)]
    f.writelines(a)
    b = [str(i) + "\n" for i in range(100)]
    f.writelines(b)
    print(f.read())


# Pandas部分

# pandas IO, 默认读入的文件是Dataframe
import pandas as pd

csv_data_path = './data/wanke_data.csv'

wanke_csv = pd.read_csv(csv_data_path)
print(wanke_csv.head())

# Save/load the dataframe from the pickle file
pickle_path = './data/wanke_data.pkl'
wanke_csv.to_pickle(pickle_path)
wanke_new_pickle = pd.read_pickle(pickle_path)
print("=" * 30)
print("Shapes of wanke_csv and wanke_pickle are the same?", wanke_csv.shape == wanke_new_pickle.shape)
print(wanke_new_pickle.head())

# Save/load the dataframe from the above excel file
excel_path = './data/wanke_data.xlsx'
wanke_csv.to_excel(excel_path, index=False)
wanke_new_excel = pd.read_excel(excel_path)
print("=" * 30)
print("Shapes of wanke_csv and wanke_excel are the same?", wanke_csv.shape == wanke_new_excel.shape)
print(wanke_new_excel.head())

# Save/load the dataframe from the above html file
html_path = './data/wanke_data.html'
wanke_csv.to_html(html_path, index=False)
wanke_new_html = pd.read_html(html_path)[0]
print("=" * 30)
print("Shapes of wanke_csv and wanke_html are the same?", wanke_csv.shape == wanke_new_html.shape)
print(wanke_new_html.head())

# Pandas Demo

import pandas as pd
import pickle

df = pd.read_csv('./data/wanke_data.csv')
print("Successfully read the file")
with open("./data/wanke_data.pkl","wb") as wf:
    pickle.dump(df,wf)
print("Successfully save the df in pickle")
del df
print("reload the df from the file")
df = pd.read_pickle('./data/wanke_data.pkl')
print(df.head())
print('='*40) # 语法糖，分割线
print(df.describe()) # 统计描述
print('='*40)
print(df.info()) # 行列信息，数据类型
print('='*40)
print(df.index) # 索引的信息
print('='*40)
print('='*40)
low2high=df[df['Open']<df['Close']][['Open','Close']] # 索引并选取
print(low2high.head())
print(low2high.shape)
print(len(low2high))
print("df['Open'].mean()=",df['Open'].mean())
print(f"df['Open'].std()={df['Open'].std()}")
print('='*40)
df['Open']+=5
print(f"df['Open'].mean()={df['Open'].mean()}")

print('='*40)

def minus5(x):
    return x-5

df['Open']=df['Open'].apply(minus5) # 使用apply方法
print(f"df['Open'].mean()={df['Open'].mean()}")
print('='*40)
print('='*40)
df['l2h'] = df['Open']<df['Close']
print(df.head())
print('='*40)
print(df.groupby('l2h')['Volume'].mean())


# iloc使用索引，loc
# pandas.DataFrame.set_index("",inplace = True) , return None
# pandas.DataFrame = pandas.DataFrame.reset_index("") (copy一个新的)
# pd.loc[["","",""],["open","close"]] 先行后列
# wanke_new["Open"] < wanke_new["Close"] 返回一个series
#  += 语法糖


#Numpy
"""
matrix 
Numpy ndarray 只能包含numeric数据

df.to_numpy()    df.values

"""


# Data Collection

# Tushare

import tushare as ts


#（your token可以在免费注册后，个人主页的“接口Token”下找到）
api = ts.pro_api("128c6908532bde66c7594f02b66e210139c2ce2c175484358d477c30")
result = api.daily(ts_code='000001.SZ', start_date='20200214', end_date='20200220')
result.to_excel('./week3/data/sz000001.xlsx')

# web scrapping _ process

"""

5开头的时候，服务端准备数据有问题


HTTP hyper text

"""


import requests
response = requests.get("http://httpbin.org/headers")
print(response.status_code)
print(response.text)
"""
{
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.24.0", 
    "X-Amzn-Trace-Id": "Root=1-6018405c-12110bee377646765930b27e"
  }
  
"""
# print(dir(response))
print([i for i in dir(response) if "__" not in i])


# http 课件codes
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


"""

Session 会话
同一个会话之中才可能维持cookie
"""

# 创建cookie
# session can persist cookie
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'


print("\n","="*30, "Failed Cookie")
# request CANNOT persist cookie

requests.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = requests.get('https://httpbin.org/cookies')   # 不同会话

print(r.text)
# '{"cookies": {}}'




# json_crawler
"""
JSON(JavaScript Object Notation, JS 对象简谱) 是一种轻量级的数据交换格式。
它基于 ECMAScript (欧洲计算机协会制定的js规范)的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。
简洁和清晰的层次结构使得 JSON 成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。
JSON是一个标记符的序列。这套标记符包含六个构造字符、字符串、数字和三个字面名。
JSON 是 JS 对象的字符串表示法，它使用文本表示一个 JS 对象的信息，本质是一个字符串。
任何支持的类型都可以通过 JSON 来表示，例如字符串、数字、对象、数组等。但是对象和数组是比较特殊且常用的两种类型。
对象：对象在 JS 中是使用花括号包裹 {} 起来的内容，数据结构为 {key1：value1, key2：value2, ...} 的键值对结构。
在面向对象的语言中，key 为对象的属性，value 为对应的值。键名可以使用整数和字符串来表示。值的类型可以是任意类型。

数组：数组在 JS 中是方括号 [] 包裹起来的内容，数据结构为 ["java", "javascript", "vb", ...] 的索引结构。
在 JS 中，数组是一种比较特殊的数据类型，它也可以像对象那样使用键值对，但还是索引使用得多。同样，值的类型可以是任意类型。


XML天生有很好的扩展性，JSON当然也有，没有什么是XML可以扩展而JSON却不能扩展的。
不过JSON在Javascript主场作战，可以存储Javascript复合对象，有着xml不可比拟的优势。
"""

import json
import requests
fake_header = {  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2"
        }
# json.cn
s = requests.Session()

r=s.get('https://xueqiu.com',headers = fake_header)
r = s.get('https://xueqiu.com/query/v1/symbol/search/status?u=251611751531466&uuid=1354410714076434432&count=10&comment=0&symbol=TSLA&hl=0&source=all&sort=time&page=1&q=&type=0&session_token=null&access_token=176b14b3953a7c8a2ae4e4fae4c848decc03a883',headers = fake_header)

# print(r.text)
# parsed_json = r.json
parsed_json = json.loads(r.text)
print(parsed_json["list"][0]['text'])

# <h4> 高亮


