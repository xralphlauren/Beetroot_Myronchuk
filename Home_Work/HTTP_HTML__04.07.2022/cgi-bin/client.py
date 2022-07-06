#coding:utf-8
import sys
import cgi
import html
import sqlite3
sys.path.insert(0, "D:\\mk")
sys.path.insert(0, 'D:\\mk\\lib\\site-packages')
sys.stdout.reconfigure(encoding="utf-8")



form = cgi.FieldStorage()
inp_id = form['id_form'].value

con = sqlite3.connect('../chinook.db')
cur = con.cursor()
query = cur.execute(f'SELECT * FROM customers WHERE CustomerId = {inp_id}').fetchall()

print("Content-type: text/html")
print()
print(f"{query}<br><br>")
