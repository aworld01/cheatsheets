"""
This read-only property returns the number of rows returned for SELECT statements, or the number of rows affected by DML statements such as INSERT or UPDATE.
Syntax:
    cur.rowcount
"""
import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")
cur = con.cursor()
try:
    cur.execute("""DELETE FROM Students WHERE id=14""")
    con.commit()
    print(cur.rowcount, "Row deleted....") #to count inserted, deleted rows
except:
    con.rollback()
    print("Unable to deleted....")
cur.close()
con.close()