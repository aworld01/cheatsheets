import sqlite3

conn = sqlite3.connect('test.db') #to create and connect to database;

## to insert data from variables
def insertdata(task):
    query = "INSERT INTO todo(task) VALUES(?);"
    conn.execute(query, (task,))
    conn.commit() #to append the table values

## to delete data from variables
def deletebyid(taskid):
    query = "DELETE FROM todo WHERE id = ?;"
    conn.execute(query, (taskid,))
    conn.commit() #to append the table values

def updatedata(taskid, newtask):
    query = "UPDATE todo SET task = ? WHERE id = ?;"
    conn.execute(query, (newtask, taskid))
    conn.commit()

conn.execute('''CREATE TABLE IF NOT EXISTS todo(
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL
);
''') #to create a table

##to add values
# query = "INSERT INTO todo(task) VALUES('Record');"
# conn.execute(query)
# conn.commit() #to append the table values

# insertdata('Have break') #to insert
# deletebyid(5) #to delete
updatedata(2, 'Hello Abdul') #to update

##to access the table
query = "SELECT * FROM todo"
for rows in conn.execute(query):
    print(rows)

conn.close() #to close the connection