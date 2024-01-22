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
while isDone == False:
    
    choice = input("Please enter an option for your list of sales: \n1. Read table \n2. Add a new entry \n3. Update an entry\
               \n4. Delete an entry \n5. Exit \n")

    if choice == '1':
     #Executing a query to select the whole table
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM [PracticeDatabase].[dbo].[SalesOrders$]")
        row = cursor.fetchone() 
        while row:
            print (row) 
            row = cursor.fetchone()

    elif choice ==  '2':
        # Asks the user for data for new order.
        region = input("Please enter the region: ")
        rep = input("Please enter the name of the sales representative: ")
        item = input("Please enter the name of the item: ")
        units = float(input("Please enter the number of items that have been bought: "))
        cost = float(input("Please enter the cost of the item: "))
        total = units * cost
        date = datetime.now()

        # Grabs the largest order ID to find new order ID of the added entry.
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(OrderID) FROM [PracticeDatabase].[dbo].[SalesOrders$]")
        max = cursor.fetchval()
        
        # Inserts the new row
        cursor.execute("INSERT INTO [PracticeDatabase].[dbo].[SalesOrders$] ([OrderDate], [Region], [Rep], [Item], [Units], [Unit Cost], [Total], [OrderID])\
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (date, region, rep, item, units, cost, total, max + 1))
        connection.commit()

    elif choice == '3':
 
      
       orderChoice = input("Please enter which order you would like to update by entering its order ID ")
       
       # Allows continuous updating until the user is done modifying the sales order.
       updateDone = False
       cursor = connection.cursor()
       date = datetime.now()
       while updateDone == False:
           change = input("What would you like to change? \n1. Region \n2. Rep \n3. Item \n4. Units \n5. Cost \n6. Finish updating \n")
           if change == '1':
               region = input("Please enter the new region: ")
               cursor.execute("UPDATE [PracticeDatabase].[dbo].[SalesOrders$] SET OrderDate = ?, Region = ?  WHERE OrderID = ?", (date), (region), (orderChoice))
               connection.commit()
           elif change == '2':
               rep = input("Please enter the new sales representative: ")
               cursor.execute("UPDATE [PracticeDatabase].[dbo].[SalesOrders$] SET OrderDate = ?, Rep = ?  WHERE OrderID = ?", (date), (rep), (orderChoice))
               connection.commit()
           elif change == '3':
               item = input("Please enter the name of the new item: ")
               cursor.execute("UPDATE [PracticeDatabase].[dbo].[SalesOrders$] SET OrderDate = ?, Item = ?  WHERE OrderID = ?", (date), (item), (orderChoice))
               connection.commit()
           elif change == '4':
               units = float(input("Please enter the new number of units: "))
               
               # Grabs the cost of the item in order to recalculate the total cost
               cursor.execute("SELECT [Unit Cost] FROM [PracticeDatabase].[dbo].[SalesOrders$] WHERE OrderID = ?", (orderChoice))
               cost = cursor.fetchval()
               total = units * cost
               
               cursor.execute("UPDATE [PracticeDatabase].[dbo].[SalesOrders$] SET OrderDate = ?, Units = ?, Total = ?  WHERE OrderID = ?", (date), (units), (total), (orderChoice))
               connection.commit()
           elif change == '5':
                cost = float(input("Please enter the new cost: "))
                
                # Grabs the number of units in order to recalculate the total cost
                cursor.execute("SELECT [Units] FROM [PracticeDatabase].[dbo].[SalesOrders$] WHERE OrderID = ?", (orderChoice))
                units = cursor.fetchval()
                total = units * cost
                
                cursor.execute("UPDATE [PracticeDatabase].[dbo].[SalesOrders$] SET OrderDate = ?, [Unit Cost] = ?, Total = ?  WHERE OrderID = ?", (date), (cost), (total), (orderChoice))
                connection.commit()
           elif change == '6':
               updateDone = True
       
    elif choice == '4':
        
        orderChoice = input("Please enter the order ID to delete. ")
        
        # Delete Row
        cursor = connection.cursor()
        cursor.execute("DELETE FROM [PracticeDatabase].[dbo].[SalesOrders$] WHERE OrderID = ?", (orderChoice))
        connection.commit()
    
    elif choice == '5':
        isDone = True



