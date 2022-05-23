import mysql.connector

con = mysql.connector.connect(host="localhost", username="thor")
cur = con.cursor()

cur.execute("SHOW DATABASES")

"""to check database in list"""
# print(cur.fetchall())

"""to check databases in tuple"""
for database in cur:
    print(database)

con.close()