"""
Update data in table - tuple
"""
# import mysql.connector
# try:
#     con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
#     if con.is_connected():
#         print("Connected....")
# except:
#     print("Unable to connect....")

# sql = "UPDATE students SET fees=%s WHERE id=%s"
# """Input from User"""
# i = int(input("Enter id to update: "))
# f = float(input("Enter the Fees: "))

# prams = (f,i)
# cur = con.cursor()
# try:
#     cur.execute(sql, prams)
#     con.commit()
#     print(cur.rowcount, "Row Updated....")
# except:
#     con.rollback()
#     print("Unable to Update data....")
# cur.close()
# con.close()



"""
Update data in table - dictionary
"""
import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")

sql = "UPDATE students SET fees=%(fees)s WHERE id=%(id)s"
"""Input from User"""
i = int(input("Enter id to update: "))
f = float(input("Enter the Fees: "))

prams = {"fees": f, "id": i}
cur = con.cursor()
try:
    cur.execute(sql, prams)
    con.commit()
    print(cur.rowcount, "Row Updated....")
except:
    con.rollback()
    print("Unable to Update data....")
cur.close()
con.close()