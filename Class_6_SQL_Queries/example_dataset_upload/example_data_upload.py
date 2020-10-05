#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:23:34 2020

@author: hantswilliams


# Note -> if doing this in google colab jupyter notebook, just be sure to add these
# to install drivers/packages:
    
!sudo apt-get install python3-dev default-libmysqlclient-dev
!pip install pymysql SQLAlchemy    
    
    
### to upload files: 
    
from google.colab import files
import io 

uploaded = files.upload()
df = pd.read_csv(io.BytesIO(uploaded['Filename.csv']))





"""



#Packages for SQL CONNECTION 
from sqlalchemy import create_engine
import sqlalchemy 

#Packages for DATAFRAME 
import pandas as pd


### Lets load our CSV file from GITHUB: 
file1 = pd.read_csv('https://raw.githubusercontent.com/hantsw/statistics/master/data_meds_ph.csv')
file2 = pd.read_csv('https://raw.githubusercontent.com/hantsw/statistics/master/data_meds_ph.csv')
file3 = pd.read_csv('https://raw.githubusercontent.com/hantsw/statistics/master/data_meds_ph.csv')
file4 = pd.read_csv('https://raw.githubusercontent.com/hantsw/statistics/master/data_meds_ph.csv')
file5 = pd.read_csv('https://raw.githubusercontent.com/hantsw/statistics/master/data_meds_ph.csv')


MYSQL_HOSTNAME = 'xx'
MYSQL_USER = 'xx'
MYSQL_PASSWORD = 'xx'
MYSQL_DATABASE = 'xx'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

### Test connection 
print (engine.table_names())


### Insert 
file1.to_sql('table1', con=engine, if_exists='append')
file2.to_sql('table2', con=engine, if_exists='append')
file3.to_sql('table3', con=engine, if_exists='append')
file4.to_sql('table4', con=engine, if_exists='append')
file5.to_sql('table5', con=engine, if_exists='append')


### Test 
test_v1 = pd.read_sql("select * from table1 limit 5;", con=engine)
