"""
commit() method: This method is used to save inserted row in the table. It is required to make the changes, otherwise no changes are made to the table.
This method sends a COMMIT statement of the MySQL server committing the current transaction. Since by default Connector/Python doesn't autocommit it's important to call this method after every transation that modifies data for tables that use transctional storage engines.
Syntax:-
    con.commit()

rollback() method: This method is used to un-save row if there is an error.
This method sends a rollback statement of the MySQL server undoing all data changes from the current transaction. By defauld, Connector/Python doesn't autocommit, so it's possible to cancel transctions when using transactional storage engines such as InnoDB.
Syntax:-
    con.rollback()
eg:-
try:
    cur.execute(query)
    con.commit()
except:
    con.rollback()

5:48/16:20
"""
import mysql.connector

try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")
cur = con.cursor()

"""insert a single record"""
# try:
#     cur.execute("INSERT INTO Students(name, roll, fees) VALUES('Abdul Zoha', 28, 2000)")
#     con.commit()
#     print("The record has been inserted")
# except:
#     con.rollback()
#     print("Unable to insert record....")

"""insert multiple records"""
# try:
#     cur.execute("""INSERT INTO Students(name, roll, fees) VALUES
#     ('Jai', 103, 3000),
#     ('Veeru', 104, 4000),
#     ('Basanti', 105,5000)
#     """)
#     con.commit()
#     print("The record has been inserted....")
# except:
#     con.rollback()
#     print("Unable to insert record....")

"""check table"""
cur.execute("SELECT * FROM Students")
for records in cur:
    print(records)

cur.close()
con.close()