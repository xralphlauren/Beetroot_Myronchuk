#coding:utf-8
import sys
sys.path.insert(0, "D:\\mk")
sys.path.insert(0, 'D:\\mk\\lib\\site-packages')
sys.stdout.reconfigure(encoding="utf-8")

import os


print("Content-type: text/html")
print()
for v in os.environ:
    if v == 'QUERY_STRING':
        for i in os.environ[v].split('&'):
            print(f"<p>{i}</p>")
