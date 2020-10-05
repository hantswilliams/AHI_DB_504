#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:06:48 2020

@author: hantswilliams
"""

import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine


neelam = pd.DataFrame({'colors' : ['blue', 'purple', 'pink']})


MYSQL_HOSTNAME = '3.84.158.190'
MYSQL_USER = 'dba'
MYSQL_PASSWORD = 'ahi2020'
MYSQL_DATABASE = 'populationhealth'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

neelam.to_sql('neelam_colors', con=engine)