import mysql.connector

con = mysql.connector.connect(user="thor", host="localhost", database="myDatabase")
cur = con.cursor()

"""to insert records in bulk"""
# query = "INSERT INTO Students(name, age) VALUES(%s,%s)"
# val = [
#     ("Abdul Samad", 31),
#     ("Shaquib", 25),
#     ("Hasan", 45),
#     ("Waseem", 55),
#     ("Waheed", 23),
#     ("Raju", 25),
#     ("Zainab", 18)
# ]
# cur.executemany(query, val)
# con.commit()

"""check table"""
query = "SELECT * FROM Students"
cur.execute(query)
for row in cur:
    print(row)

con.close()