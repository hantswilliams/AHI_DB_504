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


## V1 
mergedAllergies_patients = allergies.merge(patients, 
                                           how='left', 
                                           left_on='PATIENT', 
                                           right_on='Id')

mergedAllergies_patients = allergies.merge(patients, 
                                           how='left', 
                                           left_on='PATIENT', 
                                           suffixes=('_tab1', '_tab2'),
                                           right_on='Id')
## V2 
mergedAllergies_patients = pd.merge(allergies, 
                                    patients, 
                                    how='left', 
                                    left_on='PATIENT', 
                                    right_on='Id')


"""

SELECT *
FROM patients
LEFT JOIN allergies 
ON allergies.patient = patients.id;

"""

mergedPatients_allergies = pd.merge(patients, 
                                    allergies,
                                    how='left', 
                                    left_on='Id',
                                    right_on='PATIENT')



#### CONCAT - how do we then merge 2 tables together with same columns / 
## give us additional rows 

dataframe1 = patients.sample(10)
dataframe2 = patients.sample(10)

dataframe3 = pd.concat([dataframe1, dataframe2])


### creating an error 
dataframe3 = pd.concat([dataframe1, allergies])
### never do this 



### PYTHON FUNCTION 


def gendermodifier(varname):
    dataframe1['GENDER'] = 'the gender of this person is: ', dataframe1['GENDER']


gendermodifier()


    














