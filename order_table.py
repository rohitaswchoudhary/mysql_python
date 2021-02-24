import mysql.connector

mydb = mysql.connector.connect(
host='localhost',
user='root',
password='Rohitasw@2002',
database = "mydatabase"
)
mycursor = mydb.cursor()

# Sort the Result
# Use the ORDER BY statement to sort the result in ascending or descending order.

# The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.


sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
print()

# ORDER BY DESC
# Use the DESC keyword to sort the result in a descending order.

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)









