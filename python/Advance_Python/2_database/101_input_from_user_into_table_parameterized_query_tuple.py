"""
Insert Single Row - Input from User - tuple
"""
# import mysql.connector
# try:
#     con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
#     if con.is_connected():
#         print("Connected....")
# except:
#     print("Unable to connect....")
# sql = "INSERT INTO students(name, roll, fees) VALUES(%s, %s, %s)"
# """user_input"""
# nm = input("Enter your name: ")
# ro = int(input("Enter Roll: "))
# fe = float(input("Enter Fees: "))

# prams = (nm, ro, fe)
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
Insert Multiple Rows - Input from User - tuple
"""

import mysql.connector
def student_data(nm, ro, fe):
    try:
        con = mysql.connector.connect(user="thor", host="localhost", port=3306, database="pdb")
        if con.is_connected():
            print("Connected....")
    except:
        print("Unable to connect....")
    sql = "INSERT INTO students(name, roll, fees) VALUES(%s, %s, %s)"
    prams = (nm, ro, fe)
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
    """user_input"""
    nm = input("Enter your name: ")
    ro = int(input("Enter Roll: "))
    fe = float(input("Enter Fees: "))
    student_data(nm, ro, fe)
    print()
    ans = input("Do you want to exit? (y/n): ").lower()
    if ans == "y":
        break
