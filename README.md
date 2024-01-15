# Description
A Python script that accesses a local database that contains a table of sales orders in SQL Server.

# Functions
### Add an Entry

Allows you to enter a new sales order by filling in a series of properties (region, item, price, etc.). After filling out the entry, the date/time, order ID number, and total cost of the item is automatically input into the table.

### Delete an Entry

Allows you to delete a row by entering the sale's order ID.

### Update an Entry

Asks the user to choose a row to edit by order ID, then asks what property of the sale should be edited such as region, item, etc.. The date/time is also updated and also the total price if applicable upon editing. The order can be edited until the user exits.

### View Table

Displays the table.

# References and Other Notes
The spreadsheet was obtained from sample data file 1 - "Office Supply Sales" from the following link: https://www.contextures.com/xlsampledata01.html

An additional column was made for order ID.