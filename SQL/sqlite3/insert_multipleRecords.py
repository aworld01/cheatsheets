import sqlite3

con = sqlite3.connect("myDatabase.db")
cur = con.cursor() #to create a cursor
customers = [("Ramu", 20, "ramu@gmail.com"), ("Shamu", 25, "shamu@gmail.com")]
cur.executemany("INSERT INTO Customer VALUES(?,?,?)", customers)
con.commit()
con.close()