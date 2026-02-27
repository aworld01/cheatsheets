import mysql.connector

try:
    con = mysql.connector.connect(
    user='thor',
    host='localhost',
    port=3306,
    database='pdb' #to create a connection with database
    )
    if con.is_connected(): #to check a connection
        print('Connected....')
except:
    print("Unable to connect....")

con.close()