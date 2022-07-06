import os

# task 3
path = 'C:\Python\PyCharm\Myronchuk_Beetroot\Home_Work\HTTP_HTML__02.07.2022\Task 3,4'
os.chdir(path)

lst_mp = []
for i in os.listdir():
    if i[-3:] == 'mp3':
        lst_mp.append(i)

with open(f'{path}/play_list.m3u', 'w') as m3u:
    for i in lst_mp:
        m3u.write(f'{i}\n')


# task 4
from mako.template import Template


t = Template(filename='C://Python/PyCharm/Myronchuk_Beetroot/Home_Work/HTTP_HTML__02.07.2022/Task 3,4/m3ulist.txt')
rend_list = t.render(track=lst_mp)
with open(f'{path}/play_list_rend.m3u', 'w') as m3u:
    m3u.write(rend_list)
