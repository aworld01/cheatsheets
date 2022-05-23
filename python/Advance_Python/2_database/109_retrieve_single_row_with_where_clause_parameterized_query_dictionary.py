"""
Retrieve Single Row - dictionary
"""
import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")

sql = "SELECT * FROM students WHERE id=%(id)s"
"""Input from User"""
n = int(input("Enter id to Display: "))

prams = {"id": n}
cur = con.cursor()
try:
    cur.execute(sql, prams)
    row = cur.fetchone()
    print(row)
except:
    con.rollback()
    print("Unable to Retrieve data....")
cur.close()
con.close()