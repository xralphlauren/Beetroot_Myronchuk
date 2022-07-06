import sqlite3
import sys
from jinja2 import Template


sys.stdout.reconfigure(encoding="utf-8")
con = sqlite3.connect('C://Python/PyCharm/Myronchuk_Beetroot/Home_Work/HTTP_HTML__02.07.2022/Task 1,2/chinook.db')
cur = con.cursor()

customers = cur.execute('SELECT * FROM customers;').fetchall()

con.close()

path = 'C://Python/PyCharm/Myronchuk_Beetroot/Home_Work/HTTP_HTML__02.07.2022/Task 1,2/tmpl/tabl_tml_jinja.html'
t = Template(open(path).read())

print("Content-type: text/html")
print()
print(t.render(my_table=customers))





