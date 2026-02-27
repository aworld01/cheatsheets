"""
You can use ?, and %s both into query when you use Prepared Statement
Syntax:-
    cur.con.cursor(prepared=True)
"""
"""example-1"""
# import mysql.connector
# try:
#     con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
#     if con.is_connected():
#         print("Connected....")
# except:
#     print("Unable to connect....")

# sql = "SELECT * FROM students WHERE fees=%s"
# """Input from User"""
# n = int(input("Enter fees to Display: "))

# prams = (n,)
# cur = con.cursor(prepared=True)
# try:
#     cur.execute(sql, prams)
#     for row in cur:
#         print(row)
# except:
#     con.rollback()
#     print("Unable to Retrieve data....")
# cur.close()
# con.close()




"""example-2"""
import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")

sql = "SELECT * FROM students WHERE fees=?"
"""Input from User"""
n = int(input("Enter fees to Display: "))

prams = (n,)
cur = con.cursor(prepared=True)
try:
    cur.execute(sql, prams)
    for row in cur:
        print(row)
except:
    con.rollback()
    print("Unable to Retrieve data....")
cur.close()
con.close()