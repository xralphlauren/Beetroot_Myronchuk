#coding:utf-8
import sys
sys.path.insert(0,'C://Python/venvs/mk')
sys.path.insert(0,'C://Python/venvs/mk/Lib/site-packages')
sys.stdout.reconfigure(encoding="utf-8")

import os

print("Content-type: text/html")
print()
for v in os.environ:
    if v == 'QUERY_STRING':
        print(f'<p>{v} -- {os.environ[v]}</p>')
