#coding:utf-8
import sys
sys.path.insert(0,'C://Python/venvs/mk')
sys.path.insert(0,'C://Python/venvs/mk/Lib/site-packages')

alb = []
import sqlite3
sys.stdout.reconfigure(encoding="utf-8")
con = sqlite3.connect("C://Python/PyCharm/Myronchuk_Beetroot/Class_Work/HTTP_HTML_lesson_2/chinook.db")
cur = con.cursor()
for i in cur.execute('''SELECT  Title FROM albums;'''):
    alb.append(i)


con.close()

from mako.template import Template
t = Template(filename="C://Python/PyCharm/Myronchuk_Beetroot/Class_Work/HTTP_HTML_lesson_2/tmpl/albums_table.html")

print("Content-type: text/html")
print()
print(t.render(albums=alb))
