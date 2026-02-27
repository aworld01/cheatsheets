import sqlite3

con = sqlite3.connect("trans.db")
cur = con.cursor() #to create a cursor

query = """INSERT INTO students(name, class, email) VALUES(
    "Salauddin Ansari",
    "12th",
    "salauddin7@gmail.com"
    )"""

cur.execute(query)
con.commit()

cur.close()
con.close()