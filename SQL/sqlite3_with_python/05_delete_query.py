import sqlite3

con = sqlite3.connect("sqlite.db")
cur = con.cursor() #to create a cursor

query = "DELETE FROM students WHERE name='Abdul Zoha'"
cur.execute(query)
con.commit()

cur.close()
con.close()