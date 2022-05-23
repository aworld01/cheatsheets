"""
MySQL: is an open source database management system application which will help us to manage the database like store and retrieve data.

connect(): This method is used to open or establish a new connection. It returns an object representing the connection.

close(): This method is used to close the connection.

is_connected(): This method is used to check if the connection to MySQL is established or not. It returns True if the coneection is established successfully.



option-1
Syntax:-
    import mysql.connector #pip install mysql-connector-python
    con = mysql.connector.connect(user='thor', password='kali', host='localhost', port=3306, database='myDatabase')

option-2
Syntax:-
    import mysql.connector
    con = mysql.connector.connect(
        user='thor',
        password='kali',
        host='localhost',
        port=3306,
        database='myDatabase'
    )

option-3
Syntax:-
    import mysql.connector
    config={
        'user':'thor',
        'password': 'kali',
        'host': 'localhost',
        'port': 3306,
        'database': 'myDatabase'
    }
    con = mysql.connector.connect(**config)
"""
"""
pip install mysql-connector-python
pip3 install mysql-connector
"""
import mysql.connector

# con = mysql.connector.connect(
#     user='thor',
#     host='localhost',
#     port=3306
# )
# print(con.is_connected())


"""example-1"""
# try:
#     con = mysql.connector.connect(
#     user='thor',
#     host='localhost',
#     port=3306
#     )
#     print(con.is_connected())
# except:
#     print("Unable to connect....")


"""example-2"""
"""to create a connection"""
try:
    con = mysql.connector.connect(
    user='thor',
    host='localhost',
    port=3306
    )
    if con.is_connected(): #to check a connection
        print('Connected....')
except:
    print("Unable to connect....")

con.close() #to close the connection

print(con.is_connected())