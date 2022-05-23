"""
This method retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available. By default, the returned tuple consists of data returned by the MySQL server, converted to Python objects. If the cursor is a raw cursor, no such conversion occurs.
You must fetch all rows for the current query before executing new statements using the same connection.
Syntax:-
    row = cur.fetchone()
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
    # cur.execute("SELECT * FROM Students")
    # """example-1"""
    # row = cur.fetchone()
    # while row is not None:
    #     print(row)
    #     row = cur.fetchone()

    """example-2"""
    # row = cur.fetchone()
    # while row is not None:
    #     i,n,r,f=row
    #     print(f"Id: {i}")
    #     print(f"Name: {n}")
    #     print(f"Roll: {r}")
    #     print(f"Fee: {f}")
    #     print()
    #     row = cur.fetchone()

    """example-3"""
    # row = cur.fetchone()
    # while row is not None:
    #     i = row[0]
    #     n = row[1]
    #     r = row[2]
    #     f = row[3]
    #     print(f"Id: {i}")
    #     print(f"Name: {n}")
    #     print(f"Roll: {r}")
    #     print(f"Fees: {f}")
    #     print()
    #     row = cur.fetchone()



    # cur.execute("SELECT roll FROM Students")
    # row = cur.fetchone()
    # while row is not None:
    #     print(row)
    #     row = cur.fetchone()


    # cur.execute("SELECT id, fees FROM Students")
    # row = cur.fetchone()
    # while row is not None:
    #     print(row)
    #     row = cur.fetchone()

    
    cur.execute("SELECT * FROM Students")
    for row in cur:
        print(row)

    print("Total rows:",cur.rowcount)
except:
    con.rollback()
    print("Unable to update data....")
cur.close()
con.close()