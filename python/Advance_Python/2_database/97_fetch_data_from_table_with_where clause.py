import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database='pdb')
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")
cur = con.cursor()
try:
    cur.execute("SELECT * FROM Students WHERE name='Sumit'")
    for row in cur:
        print(row)

    print("Total rows:",cur.rowcount)
except:
    con.rollback()
    print("Unable to update data....")
cur.close()
con.close()