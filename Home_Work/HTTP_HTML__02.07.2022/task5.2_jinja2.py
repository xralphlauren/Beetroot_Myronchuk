import jinja2 as j2

template = j2.Template(open('tmpl.txt').read())
print(template.render(name='MEDVED'))