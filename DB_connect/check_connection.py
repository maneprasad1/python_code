# -*- coding: utf-8 -*-
"""
Created on Mon May  8 14:46:18 2023

@author: cdacstaff
"""

#pip install mysql-connector-python

import mysql.connector # type: ignore

cnx = mysql.connector.connect(user='root', 
                              password='PrasadM@2003',
                              host='127.0.0.1',
                              database='iacsddbda2025')
cnx.close()