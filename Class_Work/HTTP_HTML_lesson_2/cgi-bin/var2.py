#coding:utf-8
import sys
sys.path.insert(0,'C://Python/venvs/mk')
sys.path.insert(0,'C://Python/venvs/mk/Lib/site-packages')
sys.stdout.reconfigure(encoding="utf-8")

import os
import cgi

print("Content-type: text/html")
print()

print(cgi.FieldStorage())
