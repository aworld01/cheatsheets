"""
Insert Single Row - dictionary
"""
import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")

sql = "INSERT INTO students(name, roll, fees) VALUES(%(name)s, %(roll)s, %(fees)s)"
# prams = {"name": "Sameer", "roll": 777, "fees": 54100}
prams = {"roll": 111, "name": "Kunal", "fees": 3400} #no need to maintain order
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