"""
(A) cursor() method: This method is used to create cursor class object.
We need cursor object so we can call execute() method.
Syntax:-
    cur = con.cursor()

Arguments may be passed to the cursor() method to control what type of cursor to create:-

1: If buffered is True, the cursor fetches all rows from the server after an operation is executed. This is useful when queries return small result sets. buffered can be used alone, or in combination with the dictionary or named_tuple argument.

2: If dictionary is True, the cursor returns rows as dictionaries.

3: If named_tuple is True, the cursor returns rows as named tuples.

4: If prepared is True, the cursor is used for executing prepared statements.

5: If row is True, the cursor skips the conversion from MySQL datatypes to Python types when fetching rows. A raw cursor is usually used to get better performance or when you want to do the conversion yourself.

6: The cursor_class argument can be used to pass a class to use for instanitiating a new cursor. It must be a subclass of cursor.CursorBase.

The returned object depends on the combination of the arguments.
Example:-
    If not buffered and not row: MySQLCursor
    If buffered and not raw: MySQLCursorBuffered
    If not buffered and raw: MySQLCursorRaw
    If buffered and raw: MySQLCursorBufferedRaw

Examples:-
    myc = con.cursor() #MySQLCursor
    myc = con.cursor(buffered=True) #MySQLCursorBuffered
    myc = con.cursor(prepared=True) #MySQLCursorPrepared

(B) execute() mehthod: This method is used to execute given SQL queries.
We need cursor object so we can call execute() method.
Syntax:-
    con.cursor(sql, param=None, multi=False)
Param: The parameters found in the tuple or dictionary params are bound to the variables in the operation.
Multi: execute() returns an iterator if multi is True.
Syntax:-
    cur = con.cursor()
    cur.execute('SELECT * FROM students')

    q = 'SELECT * FROM students'
    cur = con.cursor()
    cur.execute(q)

(C) close() method: This method closes the cursor, resets all results, and ensures that the cursor object has no reference to its original connection object.
Syntax:-
    cur.close()
"""

import mysql.connector

try:
    con = mysql.connector.connect(
    user='thor',
    host='localhost',
    port=3306
    )
    if con.is_connected(): #to check a connection
        print('Connected....')
except:
    print("Unable to connect....")

"""Create database"""
# cur = con.cursor()
# cur.execute('CREATE DATABASE pdb')
# cur.close()

"""see databases"""
cur = con.cursor()
cur.execute('SHOW DATABASES')
for d in cur:
    print(d)
cur.close()

con.close() #to close the connection