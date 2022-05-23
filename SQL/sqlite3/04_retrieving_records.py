import sqlite3

con = sqlite3.connect("sqlite.db")
data = con.execute("SELECT * FROM students")

"""example-1"""
for records in data:
    print(records) #it will returns records in tuple form

"""example-2"""
# for records in data:
#     print("ID:",records[0])
#     print("Name: ",records[1])
#     print("Class: ",records[2])
#     print("Email: ",records[3])
#     print()
    
"""example-3"""
# for records in data:
#     s_id, name, cls, email = records
#     print("id",s_id)
#     print("Name:",name)
#     print("Class:",cls)
#     print("Email:",email)
#     print()


# r = data.fetchone() #it will return first record in tuple
# print(r)



# r = data.fetchall() #it will return a list of tuple of all records
# print(r)

# for item in r:
#     print(item)


# r = data.fetchmany(3) #it will return a list of tuple how many arguments you pass.
# print(r)

con.close()