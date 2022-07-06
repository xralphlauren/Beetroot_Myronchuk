#coding:utf-8
import sys
sys.path.insert(0, "D:\\mk")
sys.path.insert(0, 'D:\\mk\\lib\\site-packages')
sys.stdout.reconfigure(encoding="utf-8")

alb = []
import sqlite3
con = sqlite3.connect("D:\\chinook.db")
cur = con.cursor()
for i in cur.execute('''SELECT Title FROM albums;'''):
    alb.append(i[0])
    
con.close()

from mako.template import Template
t = Template(filename = "D:\\html\\tmpl\\albums_table.html")

print("Content-type: text/html")
print()
print(t.render(albums = alb))
