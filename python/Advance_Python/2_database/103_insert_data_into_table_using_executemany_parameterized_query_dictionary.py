"""
Insert Multiple Rows - dictionary
"""
import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")

sql = "INSERT INTO students(name, roll, fees) VALUES(%(name)s, %(roll)s, %(fees)s)"
prams = [
    {"name": "Ajay", "roll": 124, "fees": 5426.23},
    {"name": "Rani", "roll": 845, "fees": 845621.23},
    {"name": "Rohit", "roll": 659, "fees": 47426.23}
    ]
cur = con.cursor()
try:
    cur.executemany(sql, prams) #to insert multiple values
    con.commit()
    print(cur.rowcount, "Row inserted....")
    print(f"ID is: {cur.lastrowid}")
except:
    con.rollback()
    print("Unable to Insert data....")
cur.close()
con.close()