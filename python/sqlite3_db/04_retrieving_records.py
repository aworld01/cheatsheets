import sqlite3

con = sqlite3.connect("trans.db")
cur = con.cursor()

query = "SELECT * FROM students"
cur.execute(query)

"""to get records in tuple form"""
for records in cur:
    print(records)

"""to hold records in variables"""
# for record in cur:
#     Id , name, Class, email = record
#     """to print"""
#     print(f"ID {Id}")
#     print(f"Name: {name}")
#     print(f"Class: {Class}")
#     print(f"Email: {email}")
#     print()

cur.close()
con.close()