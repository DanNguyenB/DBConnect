# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:55:19 2023

@author: danng
"""

import pyodbc
from datetime import datetime


# Creating a connection to the "PracticeDatabase" Database
connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                            "Server=desktop-bkkm8bg\sqlexpress;"
                            "Database=PracticeDatabase;"
                            "Trusted_Connection=yes;")

isDone = False
#while isDone == False:
    
#choice = input("Please enter an option for your list of sales: \n1. Read table \n2. Add a new entry \n3. Update an entry\
               #\n4. Delete an entry \n5. Exit \n")

#if choice == '1':
    # Executing a query to select the whole table
    #cursor = connection.cursor()
    #cursor.execute("SELECT * FROM [PracticeDatabase].[dbo].[SalesOrders$]")
    #row = cursor.fetchone() 
    #while row:
        #print (row) 
        #row = cursor.fetchone()

#elif choice == '2':

#else
    
# Inserting a new row into the table
# region = input("Please enter the region: ")
# rep = input("Please enter the name of the sales representative: ")
# item = input("Please enter the name of the item: ")
# units = float(input("Please enter the number of items that have been bought: "))
# cost = float(input("Please enter the cost of the item: "))
# total = units * cost
# date = datetime.now()

# cursor = connection.cursor()
# cursor.execute("INSERT INTO [PracticeDatabase].[dbo].[SalesOrders$] ([OrderDate], [Region], [Rep], [Item], [Units], [Unit Cost], [Total])\
#                VALUES (?, ?, ?, ?, ?, ?, ?)", (date, region, rep, item, units, cost, total))
# connection.commit()

# Update row
#cursor = connection.cursor()
#cursor.execute("UPDATE [PracticeDatabase].[dbo].[SalesOrders$] SET Region = 'West' WHERE Total = 545.58")
#connection.commit()


# Delete Row
#cursor = connection.cursor()
#cursor.execute("DELETE FROM [PracticeDatabase].[dbo].[SalesOrders$] WHERE Total = 8.5")
#connection.commit()



