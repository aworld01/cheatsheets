import sqlite3

con = sqlite3.connect("sqlite.db")
cur = con.cursor()

query = "SELECT * FROM students"
cur.execute(query)

"""to get records in tuple form"""
for records in cur:
    print(records)

"""to retrieving_selected_records"""
# for records in cur:
#     print("Name: ",records[1])
#     print("Class: ",records[2])
#     print("Email: ",records[3])
#     print()

"""to hold records in variables"""
# for record in cur:
#     Id , name, Class, email = record
#     """to print"""
#     print(f"ID {Id}")
#     print(f"Name: {name}")
#     print(f"Class: {Class}")
#     print(f"Email: {email}")
#     print()


# data = cur.fetchone() #it will return first record in tuple
# print(data)

# data = cur.fetchall() #it will return a list of tuple of all records
# # print(data)

# for item in data:
#     print(item)


# data = cur.fetchmany(4) #it will return a list of tuple how many arguments you pass.
# for record in data:
#     print(record)

cur.close()
con.close()