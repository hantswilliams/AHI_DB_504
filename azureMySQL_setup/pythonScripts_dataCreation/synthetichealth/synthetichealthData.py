#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 15:18:00 2021

@author: hantswilliams


1 allergies.csv
2 careplans.csv
3 conditions.csv
4 devices.csv
5 encounters.csv
6 imaging_studies.csv
7 immunizations.csv
8 medications.csv
9 observations.csv
10 organizations.csv
11 patients.csv
12 payer_transitions.csv
13 payers.csv
14 procedures.csv
15 providers.csv
16 supplies.csv


DROP TABLE IF EXISTS allergies;
DROP TABLE IF EXISTS careplans;
DROP TABLE IF EXISTS conditions;
DROP TABLE IF EXISTS devices;
DROP TABLE IF EXISTS encounters;
DROP TABLE IF EXISTS imaging_studies;
DROP TABLE IF EXISTS immunizations;
DROP TABLE IF EXISTS medications;
DROP TABLE IF EXISTS observations;
DROP TABLE IF EXISTS organizations;
DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS payer_transitions;
DROP TABLE IF EXISTS payers;
DROP TABLE IF EXISTS procedures;
DROP TABLE IF EXISTS providers;
DROP TABLE IF EXISTS supplies;



with engine.connect() as con:
    con.execute('ALTER TABLE `example_table` ADD PRIMARY KEY (`ID_column`);')


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
MYSQL_DATABASE = 'synthea'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

### Test connection 
print (engine.table_names())




file1 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/allergies.csv')
file2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/careplans.csv')
file3 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/conditions.csv')
file4 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/devices.csv')
file5 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/encounters.csv')
file6 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/imaging_studies.csv')
file7 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/immunizations.csv')
file8 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/medications.csv')
file9 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/observations.csv')
file10 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/organizations.csv')
file11 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/patients.csv')
file12 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/payer_transitions.csv')
file13 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/payers.csv')
file14 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/procedures.csv')
file15 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/providers.csv')
file16 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DB_504/main/azureMySQL_setup/pythonScripts_dataCreation/synthetichealth/testData/supplies.csv')



file2 = file2.rename({'Id': 'conditionId'}, axis=1)




file1.to_sql('allergies', con=engine, if_exists='append')
print('done with allergies')


file2.to_sql('careplans', con=engine, if_exists='append')
print('done with careplans')


file3.to_sql('conditions', con=engine, if_exists='append')
print('done with conditions')


file4.to_sql('devices', con=engine, if_exists='append')
print('done with devices')


file5.to_sql('encounters', con=engine, if_exists='append')
print('done with encounters')


file6.to_sql('imaging_studies', con=engine, if_exists='append')
print('done with imaging_studies')


file7.to_sql('immunizations', con=engine, if_exists='append')
print('done with immunizations')


file8.to_sql('medications', con=engine, if_exists='append')
print('done with medications')


file9.to_sql('observations', con=engine, if_exists='append')
print('done with observations')


file10.to_sql('organizations', con=engine, if_exists='append')
print('done with organizations')


file11 = file11.drop(columns=['BIRTHPLACE'])
file11.to_sql('patients', con=engine, if_exists='append')
print('done with patients')


file12.to_sql('payer_transitions', con=engine, if_exists='append')
print('done with payer_transitions')


file13.to_sql('payers', con=engine, if_exists='append')
print('done with payers')


file14.to_sql('procedures', con=engine, if_exists='append')
print('done with procedures')


file15.to_sql('providers', con=engine, if_exists='append')
print('done with providers')


file16.to_sql('supplies', con=engine, if_exists='append')
print('done with supplies')


### Test connection 
print (engine.table_names())




