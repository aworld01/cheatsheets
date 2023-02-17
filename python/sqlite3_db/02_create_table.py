import sqlite3

con = sqlite3.connect("trans.db")
cur = con.cursor() #to create a cursor

query = """CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name VARCHAR(15),
    class VARCHAR(2),
    email VARCHAR(20)
)"""

cur.execute(query)

cur.close()
con.close()