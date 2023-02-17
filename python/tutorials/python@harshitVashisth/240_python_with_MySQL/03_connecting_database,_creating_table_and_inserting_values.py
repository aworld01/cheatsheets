import mysql.connector

con = mysql.connector.connect(user="thor", host="localhost", database="myDatabase") #to connect to database
cur = con.cursor()

# query = "CREATE TABLE Students(name VARCHAR(20), age INT(3))" #to create table

query = "INSERT INTO Students(name, age) VALUES(%s,%s)" #to insert values. (?, ?) for SQLite

val = ("Abdul Zoha", 31)
cur.execute(query, val)

con.commit()
con.close()