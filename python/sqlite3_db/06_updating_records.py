import sqlite3

con = sqlite3.connect("trans.db")
cur = con.cursor() #to create a cursor

query = "UPDATE students SET class='12th' WHERE id=2"
cur.execute(query)
con.commit()

changes = con.total_changes #to count total changes
print(f"Total Changes: {changes}")

cur.close()
con.close()