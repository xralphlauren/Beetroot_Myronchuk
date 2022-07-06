#!/usr/bin/env python3
import datetime


#path = "C://Python/PyCharm/Myronchuk_Beetroot/Home_Work/HTTP_HTML__29.06.2022/index.html"
vrem = datetime.datetime.strftime(datetime.datetime.now(), "%Y.%m.%d %H:%M:%S")
# служебные заголовки
print("Content-type: text/html")
print()
# содержимое сайта
print('''
<!DOCTYPE html>
<html class="client-nojs" lang="ru" dir="ltr">
<head>
<meta charset="UTF-8"/>''')
print('''
<body>
<html>''')
print('<title>Дата и время</title>')
print(f'<h1>Текущее время:</h1>')
print(f'<p>{vrem}</p>')

print(f'<a href="../index.html"> ссылка на Главную страницу</a>')


print('''
<body/>
<html/>''')