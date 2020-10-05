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


"""

The key variable list that we are concerned with can be found here:
    
-- Demographic data dictionary can be found here: https://wwwn.cdc.gov/Nchs/Nhanes/Search/variablelist.aspx?Component=Demographics&CycleBeginYear=2013
-- Examination data dictionary can be found here: https://wwwn.cdc.gov/Nchs/Nhanes/Search/variablelist.aspx?Component=Examination&CycleBeginYear=2013
-- Dietary data dictionary can be found here: https://wwwn.cdc.gov/Nchs/Nhanes/Search/variablelist.aspx?Component=Dietary&CycleBeginYear=2013
-- Lab data dictionary can be found here: https://wwwn.cdc.gov/Nchs/Nhanes/Search/variablelist.aspx?Component=Laboratory&CycleBeginYear=2013
-- Questionnaire data dictionary can be found here: https://wwwn.cdc.gov/Nchs/Nhanes/Search/variablelist.aspx?Component=Questionnaire&CycleBeginYear=2013


"""



#Packages for SQL CONNECTION 
from sqlalchemy import create_engine
import sqlalchemy 

#Packages for DATAFRAME 
import pandas as pd


### Lets load our CSV file from GITHUB: 
demographics = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2013_2014/demographic.csv')
diet = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2013_2014/diet.csv')
examination = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2013_2014/examination.csv')
labs = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2013_2014/labs.csv')
questionnaire = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/Class_6_SQL_Queries/example_dataset/dataset_nhanes_2013_2014/questionnaire.csv')


### Lets quickly preview, see if we need to make any chnages 
test = diet.sample(5)




MYSQL_HOSTNAME = '3.84.158.190'
MYSQL_USER = 'dba'
MYSQL_PASSWORD = 'ahi2020'
MYSQL_DATABASE = 'us_population'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

### Test connection 
print (engine.table_names())


### Insert 
demographics.to_sql('demographics', con=engine, if_exists='append')
diet.to_sql('diet', con=engine, if_exists='append')
examination.to_sql('examination', con=engine, if_exists='append')
labs.to_sql('labs', con=engine, if_exists='append')
questionnaire.to_sql('questionnaire', con=engine, if_exists='append')

### Test connection 
print (engine.table_names())


### Test 
sample = pd.read_sql("select * from demographics limit 5;", con=engine)
