import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database='pdb')
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")

cur = con.cursor()
try:
    cur.execute("UPDATE Students SET fees=300 WHERE id=17")
    con.commit()
    print(cur.rowcount, "Row updated....")
except:
    con.rollback()
    print("Unable to update data....")
cur.close()
con.close()