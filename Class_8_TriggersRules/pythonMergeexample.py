#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:08:14 2021

@author: hantswilliams
"""


# class 8 // not week 8 


import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine

MYSQL_HOSTNAME = '20.62.193.224'
MYSQL_USER = 'hantswilliams'
MYSQL_PASSWORD = 'hantswilliams2021'
MYSQL_DATABASE = 'synthea'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3305/{MYSQL_DATABASE}'
engine = create_engine(connection_string)


query1 = 'select * from patients;'
patients = pd.read_sql(query1, engine)


query2 = 'select * from allergies'
allergies = pd.read_sql(query2, engine)


### PANDAS - MERGE 

"""

SELECT *
FROM allergies
LEFT JOIN patients
ON allergies.patient = patients.id;

"""


mergedAllergies_patients = allergies.merge(patients, how='left', )













