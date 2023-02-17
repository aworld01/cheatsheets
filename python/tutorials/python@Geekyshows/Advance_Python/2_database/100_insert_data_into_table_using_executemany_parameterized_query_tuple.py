"""
executemany() method: This method is used to prepare given SQL query and executes it against all parameter sequences or mappings found in the sequence seq_of_params.
With the executemany() method, it is not possible to specify multiple statements to execute in the sql argument.
"""
import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")
sql = "INSERT INTO students(name, roll, fees) VALUES(%s, %s, %s)"
prams = [("Jai", 104, 4000), ("Veeru", 105, 5000), ("Basanti", 106, 6000)]
cur = con.cursor()
try:
    cur.executemany(sql, prams)
    con.commit()
    print(cur.rowcount, "Row inserted....")
except:
    con.rollback()
    print("Unable to Insert data....")
cur.close()
con.close()