# -- coding: utf-8 --
from jinja2 import Template

text = '''{% for item in range(5) %}
Привет {{ name }} номер {{item}}! \n
        {% endfor %}'''
template = Template(text)
print(template.render(name=u'Пользователь'))