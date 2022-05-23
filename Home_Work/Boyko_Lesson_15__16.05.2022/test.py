import datetime as dt


file = open('access-log', 'r')
wwwlog = file.readlines()
all_byte = sum((int(i.rsplit(maxsplit=1)[1]) for i in wwwlog if i.rsplit(maxsplit=1)[1].isdigit()))


dt_ip = []
[dt_ip.append(i.split(maxsplit=1)[0]) for i in wwwlog if dt.datetime.strptime(i.split()[3].split(':', maxsplit=1)[1], '%H:%M:%S').time() < dt.time(12, 00)]
print(dt_ip)

a = '04:30:40'
b = dt.datetime.strptime(a, '%H:%M:%S').time()
print(b)