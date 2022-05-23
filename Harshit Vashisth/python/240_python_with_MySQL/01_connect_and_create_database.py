"""
status; to see status of current user;
"""

import mysql.connector #pip install mysql-connector-python

con = mysql.connector.connect(host="localhost", username="thor") #to connect to mysql
cur = con.cursor() #to create a cursor

cur.execute("CREATE DATABASE myDatabase") #to execute a query

con.close()