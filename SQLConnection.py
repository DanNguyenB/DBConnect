# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:55:19 2023

@author: danng
"""

import pyodbc


# Creating a connection to the "PracticeDatabase" Database
connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                            "Server=desktop-bkkm8bg\sqlexpress;"
                            "Database=PracticeDatabase;"
                            "Trusted_Connection=yes;")

# Executing a query to select the whole table
#cursor = connection.cursor()
#cursor.execute("SELECT * FROM [PracticeDatabase].[dbo].[SalesOrders$]")
#row = cursor.fetchone() 
#while row:
    #print (row) 
    #row = cursor.fetchone()
    
# Inserting a new row into the table
cursor = connection.cursor()
cursor.execute("INSERT INTO [PracticeDatabase].[dbo].[SalesOrders$] DEFAULT VALUES")
connection.commit()

#(2023, 12, 5, 0, 0)


