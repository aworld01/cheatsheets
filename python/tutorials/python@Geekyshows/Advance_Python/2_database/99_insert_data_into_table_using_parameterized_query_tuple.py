"""Insert Single Row"""
import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")
sql = "INSERT INTO students(name, roll, fees) VALUES(%s, %s, %s)"
prams = ("Sumit", 103, 3000)
cur = con.cursor()
try:
    cur.execute(sql, prams)
    con.commit()
    print(cur.rowcount, "Row inserted....")
    print(f"ID is: {cur.lastrowid}")
except:
    con.rollback()
    print("Unable to Insert data....")
cur.close()
con.close()