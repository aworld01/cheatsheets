import sqlite3

con = sqlite3.connect("sqlite.db")
cur = con.cursor() #to create a cursor

query = """INSERT INTO students(name, class, email) VALUES(
    "Abdul Zoha",
    "10th",
    "abdulzoha786@gmail.com"
    )"""

cur.execute(query)
con.commit()

cur.close()
con.close()