"""
This method fetches the next set of rows of a query result and returns a list of tuples. If no more rows are available, it returns an empty list.
The number of rows returned can be specified using the size argument, whitch defaults to one, Fewer rows are returned if fewer rows are available than specified.
You must fetch all rows for the current query before executing new statements using the same connection.
Syntax:-
    rows = cur.fetchmany(size=5)
    rows = cur.fetchmany(5)
"""
import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database='pdb')
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")
cur = con.cursor(buffered=True) #use with fetchmany() method
try:
    cur.execute("SELECT * FROM Students")
    rows = cur.fetchmany(5)
    for row in rows:
        print(row)

    print("Total rows:",cur.rowcount)
except:
    con.rollback()
    print("Unable to update data....")
cur.close()
con.close()