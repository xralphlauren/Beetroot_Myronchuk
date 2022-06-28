import sqlite3


con = sqlite3.connect('chinook.db')
cur = con.cursor()

names = []
for s in cur.execute('SELECT * FROM customers;'):
    names.append(s[1])



print(names)
emp = cur.execute('SELECT FirstName, LastName FROM employees;')

print(emp.fetchone())           # fetchone забрать первый елемент кортежа ( как pop )
print(emp.fetchone())
print(emp.fetchall())           # fetchall забрать все елементы кортежа ( оставшиеся )

con.close()