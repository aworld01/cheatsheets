"""
Insert Single Row - dictionary
"""
# import mysql.connector
# try:
#     con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
#     if con.is_connected():
#         print("Connected....")
# except:
#     print("Unable to connect....")

# sql = "INSERT INTO students(name, roll, fees) VALUES(%(name)s, %(roll)s, %(fees)s)"
# """Input from User"""
# nm = input("Enter your name: ")
# ro = int(input("Enter your Roll: "))
# fe = float(input("Enter your Fees: "))

# prams = {"name": nm, "roll": ro, "fees": fe}
# cur = con.cursor()
# try:
#     cur.execute(sql, prams)
#     con.commit()
#     print(cur.rowcount, "Row inserted....")
#     print(f"ID is: {cur.lastrowid}")
# except:
#     con.rollback()
#     print("Unable to Insert data....")
# cur.close()
# con.close()





"""
Insert Multiple Rows - dictionary
"""
import mysql.connector
def user_data(n, r, f):
    try:
        con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
        if con.is_connected():
            print("Connected....")
    except:
        print("Unable to connect....")

    sql = "INSERT INTO students(name, roll, fees) VALUES(%(name)s, %(roll)s, %(fees)s)"
    prams = {"name": n, "roll": r, "fees": f}
    cur = con.cursor()
    try:
        cur.execute(sql, prams)
        con.commit()
        print(cur.rowcount, "Row inserted....")
        print(f"ID is: {cur.lastrowid}")
    except:
        con.rollback()
        print("Unable to Insert data....")
    cur.close()
    con.close()

while True:
    """Input from User"""
    nm = input("Enter your name: ")
    ro = int(input("Enter your Roll: "))
    fe = float(input("Enter your Fees: "))
    user_data(nm, ro, fe)
    print()

    ans = input("Do you want to exit? (y/n): ")
    if ans == "y":
        break
