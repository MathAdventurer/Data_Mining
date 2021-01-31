# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:44:35 2018

@author: Neal
"""

import sqlite3
import os

db_file='./data/stock_orders.db'
if os.path.isfile(db_file):#delete existing database file
    os.remove(db_file)
    
#connect to database    
conn = sqlite3.connect(db_file)

#create cursor 
c = conn.cursor()
# Create table with 5 column(date, trans, symbol, qty, price)
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
# Insert a batch of row data, will be faster
purchases = [('2006-01-05','BUY','RHAT',100,35.14),
             ('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
conn.close()

#use the db some other else
conn = sqlite3.connect('./data/stock_orders.db')
c = conn.cursor()
print('======List all==========')
c.execute("SELECT * FROM stocks")
print(c.fetchall())
print('\n======Search symbol=RHAT==========')
c.execute("SELECT * FROM stocks WHERE symbol='RHAT'")
print(c.fetchall())
conn.close()

