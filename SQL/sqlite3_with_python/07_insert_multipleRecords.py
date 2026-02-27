import sqlite3

con = sqlite3.connect("sqlite.db")
cur = con.cursor()

s_lists = [(4, "Raju", "5th", "raju8@gmail.com"), (5, "Rohan", "9th", "rohan44@hotmail.com"), (6, "Harry", "B.Com", "harry789@ymail.com")]

query = "INSERT INTO students VALUES(?,?,?,?)"
cur.executemany(query, s_lists) #to insert multiple values
con.commit()

cur.close()
con.close()