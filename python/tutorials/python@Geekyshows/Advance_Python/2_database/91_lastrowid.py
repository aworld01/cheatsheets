"""
This read-only property returns the value generated for an AUTO_INCREMENT column by the previous INSERT or UPDATE statement or None when there is no such value available.

If you perform an INSERT into a table that contains an AUTO_INCREMENT column, lastrowid returns the AUTO_INCREMENT value for the new row.

If you insert multiple rows into a table using a single INSERT statement, the lastrowid property contains the last insert id of the first row.
Syntax:-
    cur.lastrowid
"""
import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database='pdb')
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")

cur = con.cursor()
try:
    cur.execute("INSERT INTO Students(name, roll, fees) VALUES('Sumit', 103, 3000)")
    con.commit()
    print(cur.rowcount, "Row inserted....")
    print("Last row id is:",cur.lastrowid)
except:
    con.rollback()
    print("Unable to Inserted data....")
cur.close()
con.close()