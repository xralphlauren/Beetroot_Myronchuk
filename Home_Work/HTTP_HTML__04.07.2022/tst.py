import sqlite3
con = sqlite3.connect('chinook.db')
cur = con.cursor()
query = cur.execute(f'SELECT * FROM customers WHERE CustomerId = 7;').fetchall()
