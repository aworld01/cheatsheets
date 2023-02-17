"""
This method fetches all (or all remaining) rows of a query result set and returns a list of tuples. If no more rows are available, it returns an empty list.
You must fetch all rows for the currnet query before executing new statemants using the same connection.
Syntax:-
    rows = cur.fetchall()
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
    """example-1"""
    # cur.execute("SELECT * FROM Students")
    # for row in cur:
    #     print(row)
    
    """example-2"""
    cur.execute("SELECT * FROM Students")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    print("Total rows:",cur.rowcount)
except:
    con.rollback()
    print("Unable to update data....")
cur.close()
con.close()