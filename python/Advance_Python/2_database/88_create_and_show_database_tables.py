import mysql.connector

try:
    con = mysql.connector.connect(
        user="thor",
        host="localhost",
        database="pdb",
        port=3306
    )
    if (con.is_connected()):
        print("Connected...")
except:
    print("Unable to connect....")

"""to create table"""
# query = "CREATE TABLE Students(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), roll INT, fees FLOAT)"
# cur = con.cursor()
# cur.execute(query)

"""to check tables"""
query = "SHOW TABLES"
cur = con.cursor()
cur.execute(query)
for records in cur:
    print(records)

cur.close()
con.close()