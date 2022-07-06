import jinja2 as j2

template = j2.Template('PREVED {{ name }}!')
print(template.render(name='MEDVED'))


