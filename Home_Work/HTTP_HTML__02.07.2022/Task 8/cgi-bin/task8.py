import sys
from mako.template import Template


sys.stdout.reconfigure(encoding="utf-8")

path_m3u = 'C://Python/PyCharm/Myronchuk_Beetroot/Home_Work/HTTP_HTML__02.07.2022/Task 8/play_list.m3u'
path_mako_temp = 'C://Python/PyCharm/Myronchuk_Beetroot/Home_Work/HTTP_HTML__02.07.2022/Task 8/play_list.m3u'

list_mp3 = []
for i in open(path_m3u):
    list_mp3.append(i)


t = Template(filename=path_mako_temp)

print("Content-type: text/html")
print()
print(t.render(my_table=list_mp3))



