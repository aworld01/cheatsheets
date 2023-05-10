import sqlite3

con = sqlite3.connect('sqlite.db')
query = """CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    s_class TEXT,
    email TEXT
)"""
con.execute(query)

cur = con.cursor()

def structure():
    query = "schema students"
    data = cur(query)
    print(data)


def show():
    tables = con.execute("SELECT * FROM students")
    for records in tables:
        print(records)
    print()

def insert(name, s_class, email):
    query = "INSERT INTO students(name, s_class, email) VALUES(?,?,?)"
    con.execute(query, (name, s_class, email,))
    con.commit()
    print()

def delete(s_id):
    query = "DELETE FROM students WHERE id = ?"
    con.execute(query, (s_id,))
    con.commit()

def update(name, s_class, email, s_id):
    query = "UPDATE students SET name = ?, s_class = ?, email = ? WHERE id = ?"
    con.execute(query, (name, s_class, email, s_id))
    con.commit()

structure()