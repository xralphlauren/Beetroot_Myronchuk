#coding:utf-8
import sys
sys.path.insert(0, "D:\\mk")
sys.path.insert(0, 'D:\\mk\\lib\\site-packages')
sys.stdout.reconfigure(encoding="utf-8")

import cgi
form = cgi.FieldStorage()

import html

print("Content-type: text/html")
print()
print(f"vik --- {html.escape(form['vik'].value)}<br><br>")
'''
for f in form:
    print(f, form[f], form[f].value)
'''
