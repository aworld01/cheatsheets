import sqlite3

con = sqlite3.connect("sqlite.db")
con.execute("DELETE FROM students WHERE name='Samsul'")
con.commit()

con.close()