import sqlite3

con = sqlite3.connect("sqlite.db")
con.execute("UPDATE students SET class = '12th' WHERE s_id = '2'")
con.commit()
change = con.total_changes #to get result of total changes
print(f"Total changes {change}")

con.close()