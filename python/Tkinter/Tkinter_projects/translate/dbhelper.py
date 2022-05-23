import sqlite3

con = sqlite3.connect("dictionary.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS dict(
    id INTEGER PRIMARY KEY,
    eng TEXT NOT NULL,
    hin TEXT NOT NULL
);''')

"""functions"""
def show():
    query = 'SELECT * FROM dict'
    return cur.execute(query)
def insertdata(eng, hin):
    query = "INSERT INTO dict(eng, hin) VALUES(?,?);"
    cur.execute(query, (eng, hin))
    con.commit()
def deletebyid(taskid):
    query = "DELETE FROM dict WHERE eng = ?;"
    cur.execute(query, (taskid,))
    con.commit()
def updatedata(taskid, newtask):
    query = "UPDATE dict SET hin = ? WHERE eng = ?;"
    cur.execute(query, (newtask, taskid))
    con.commit()
def where(input):
    query = "SELECT * FROM dict WHERE eng = ?;"
    return cur.execute(query, (input,))
def count1():
    query = "SELECT COUNT(*) FROM dict"
    cur.execute(query)
    for items in cur:
        return items[0]

"""to insert data"""
# eng = input("Enter your English Word: ")
# hin = input("Enter your Hindi Word: ")
# insertdata(eng, hin)

"""to check list of data"""
# for items in show():
#     print(items)

"""to search word"""
# usr_input = input("Enter the word you want to search: ")
# for data in where(usr_input):
#     print(data)

# print(count())

# cur.close()
# con.close()