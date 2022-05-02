import sqlite3

con = sqlite3.connect("sqlite.db")
con.execute("""
INSERT INTO Students(name, class, email)
VALUES('Abdul Zoha', '10th', 'abdulzoha786@gmail.com')
""")
con.commit()

con.close()