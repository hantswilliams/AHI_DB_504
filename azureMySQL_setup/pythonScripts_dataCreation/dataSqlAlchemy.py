#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 15:18:00 2021

@author: hantswilliams
"""

import pandas as pd 
from sqlalchemy import create_engine
import sqlalchemy 
from dotenv import load_dotenv
import os

load_dotenv()

mysqluser = os.getenv('mysqluser')
mysqlpassword = os.getenv('mysqlpassword')

MYSQL_HOSTNAME = '20.62.193.224:3305'
MYSQL_USER = mysqluser
MYSQL_PASSWORD = mysqlpassword
MYSQL_DATABASE = 'ahi'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)


pandascsvfile = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_506_Research/master/Week2/final_contracts_encounters.csv')
pandascsvfile.to_sql('ph_contracts', con=engine, if_exists='append')


### Test connection 
print (engine.table_names())


### Test 
sample = pd.read_sql("select * from ph_contracts limit 5;", con=engine)


