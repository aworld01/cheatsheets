"""
Delete data from table - tuple
"""
# import mysql.connector
# try:
#     con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
#     if con.is_connected():
#         print("Connected....")
# except:
#     print("Unable to connect....")

# sql = "DELETE FROM students WHERE id=%s"
# """Input from User"""
# del_value = int(input("Enter id to delete: "))

# prams = (del_value,)
# cur = con.cursor()
# try:
#     cur.execute(sql, prams)
#     con.commit()
#     print(cur.rowcount, "Row deleted....")
# except:
#     con.rollback()
#     print("Unable to Delete data....")
# cur.close()
# con.close()




"""
Delete data from table - dictionary
"""
import mysql.connector
try:
    con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
    if con.is_connected():
        print("Connected....")
except:
    print("Unable to connect....")

sql = "DELETE FROM students WHERE id=%(id)s"
"""Input from User"""
del_value = int(input("Enter id to delete: "))

prams = {"id": del_value}
cur = con.cursor()
try:
    cur.execute(sql, prams)
    con.commit()
    print(cur.rowcount, "Row deleted....")
except:
    con.rollback()
    print("Unable to Delete data....")
cur.close()
con.close()