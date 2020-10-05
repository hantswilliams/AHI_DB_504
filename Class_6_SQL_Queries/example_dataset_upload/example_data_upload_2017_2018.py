#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:41:00 2020

@author: hantswilliams


https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2017


Dealing with XPT files which are a SAS type // 
https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.read_sas.html


Demographic Variables and Sample Weights	DEMO_J Doc	DEMO_J Data [XPT - 3.3 MB]	February 2020
Blood Pressure	BPX_J Doc	BPX_J Data [XPT - 1.4 MB]	February 2020
Body Measures	BMX_J Doc	BMX_J Data [XPT - 1.4 MB]	February 2020
Cholesterol - High - Density Lipoprotein (HDL)	HDL_J Doc	HDL_J Data [XPT - 175.5 KB]	February 2020
Physical Activity	PAQ_J Doc	PAQ_J Data [XPT - 780.9 KB]	February 2020
Medical Conditions	MCQ_J Doc	MCQ_J Data [XPT - 5.2 MB]	February 2020
Prescription Medications	RXQ_RX_J Doc	RXQ_RX_J Data [XPT - 9.2 MB]	March 2020
Hospital Utilization & Access to Care	HUQ_J Doc	HUQ_J Data [XPT - 725.1 KB]	February 2020
Mental Health - Depression Screener	DPQ_J Doc	DPQ_J Data [XPT - 477.8 KB]	February 2020
Physical Functioning	PFQ_J Doc	PFQ_J Data [XPT - 2.3 MB]	February 2020


https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2017




"""

#Packages for SQL CONNECTION 
from sqlalchemy import create_engine
import sqlalchemy 


import pandas as pd 



bmx_j = pd.read_sas('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2017_2018/BMX_J.XPT')
bpx_j = pd.read_sas('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2017_2018/BPX_J.XPT')
demo_j = pd.read_sas('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2017_2018/DEMO_J.XPT')
dpq_j = pd.read_sas('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2017_2018/DPQ_J.XPT')
hdl_j = pd.read_sas('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2017_2018/HDL_J.XPT')
huq_j = pd.read_sas('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2017_2018/HUQ_J.XPT')
mcq_j = pd.read_sas('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2017_2018/MCQ_J.XPT')
paq_j = pd.read_sas('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2017_2018/PAQ_J.XPT')
pfq_j = pd.read_sas('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2017_2018/PFQ_J.XPT')
rxq_rx_j = pd.read_sas('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DB_504/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2017_2018/RXQ_RX_J.XPT')



MYSQL_HOSTNAME = '3.84.158.190'
MYSQL_USER = 'dba'
MYSQL_PASSWORD = 'ahi2020'
MYSQL_DATABASE = 'us_population_2'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)


bmx_j.to_sql('bmx_j', con=engine, if_exists='append')
bpx_j.to_sql('bpx_j', con=engine, if_exists='append')
demo_j.to_sql('demo_j', con=engine, if_exists='append')
dpq_j.to_sql('dpq_j', con=engine, if_exists='append')
hdl_j.to_sql('hdl_j', con=engine, if_exists='append')
huq_j.to_sql('huq_j', con=engine, if_exists='append')
mcq_j.to_sql('mcq_j', con=engine, if_exists='append')
paq_j.to_sql('paq_j', con=engine, if_exists='append')
pfq_j.to_sql('pfq_j', con=engine, if_exists='append')
rxq_rx_j.to_sql('rxq_rx_j', con=engine, if_exists='append')


### Test connection 
print (engine.table_names())


### Test 
sample = pd.read_sql("select * from demo_j limit 5;", con=engine)







