import mysql.connector

mydb = mysql.connector.connect(
host='localhost',
user='root',
password='Rohitasw@2002',
database="mydatabase"
)

mycursor = mydb.cursor()

# 
# create a table.

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# check if table exists.



mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

# Primary Key
# When creating a table, you should also create a column with a unique key for each record.

# This can be done by defining a PRIMARY KEY.

# We use the statement "INT AUTO_INCREMENT PRIMARY KEY" 
# which will insert a unique number for each record. Starting at 1, 
# and increased by one for each record.

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
