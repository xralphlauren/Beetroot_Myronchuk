#coding:utf-8
import sys
sys.path.insert(0,'C://Python/venvs/mk')
sys.path.insert(0,'C://Python/venvs/mk/Lib/site-packages')
sys.stdout.reconfigure(encoding="utf-8")

cust = []
import sqlite3
con = sqlite3.connect("C://Python/PyCharm/Myronchuk_Beetroot/Class_Work/HTTP_HTML_lesson_2/chinook.db")
cur = con.cursor()

for i in cur.execute('''SELECT CustomerId, LastName, FirstName, SupportRepId FROM customers;'''):
    d = {}
    d['CustomeId'] = i[0]
    d['LastName'] = i[1]
    d['FirstName'] = i[2]
    d['SupportRepId'] = i[3]
    cust.append(d)


con.close()

from mako.template import Template
t = Template(filename="C://Python/PyCharm/Myronchuk_Beetroot/Class_Work/HTTP_HTML_lesson_2/tmpl/customers.html")
html = t.render(customers=cust)

print("Content-type: text/html")
print()
print(html)
