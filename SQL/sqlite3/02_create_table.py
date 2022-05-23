import sqlite3

con = sqlite3.connect("sqlite.db")
con.execute("""
CREATE TABLE IF NOT EXISTS students(
    s_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(15),
    class VARCHAR(10),
    email VARCHAR(30)
)
""")

con.close()