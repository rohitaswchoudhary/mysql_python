# create database


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rohitasw@2002"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

#If this page is executed with no error, you have successfully created a database.


### check if database exists

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

