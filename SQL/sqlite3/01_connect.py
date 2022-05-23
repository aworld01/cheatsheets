import sqlite3

con = sqlite3.connect("sqlite.db") #to create a connection or make database
print("\tDatabase is connected....")

con.close()