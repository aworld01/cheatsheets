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
    """example-1"""
    # cur.execute("INSERT INTO Students(name, roll, fees) VALUES('Sonam', 106, 6000)")
    # con.commit()
    # print(cur.rowcount, "Row inserted....") #rowcount example

    """example-2"""
    cur.execute("""INSERT INTO Students(name, roll, fees) VALUES
    ('Jyoti', 107, 7000),
    ('Aman', 108, 8000)
    """)
    con.commit()
    print(cur.rowcount, "Row inserted....") #to count inserted, deleted rows
except:
    con.rollback()
    print("Unable to insert Data....")
cur.close()
con.close()