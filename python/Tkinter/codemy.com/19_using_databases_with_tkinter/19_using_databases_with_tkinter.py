from tkinter import*
import sqlite3

root = Tk()
root.title("")
root.geometry("600x400")


"""DATABASE"""
"""Create a database or connect to one"""
con = sqlite3.connect("address_book.db")

"""Create a cursor"""
cur = con.cursor()

"""Create a table"""
cur.execute("""CREATE TABLE IF NOT EXISTS address(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
    )""")

"""Commite changes"""
con.commit()

"""Close connection"""
con.close()

root.mainloop()