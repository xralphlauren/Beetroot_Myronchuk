import datetime as dt


file = open('access-log', 'r')
wwwlog = file.readlines()
all_byte = sum((int(i.rsplit(maxsplit=1)[1]) for i in wwwlog if i.rsplit(maxsplit=1)[1].isdigit()))

# task 1
byte200 = sum((int(i.rsplit(maxsplit=1)[1].replace('-', '0')) for i in wwwlog if i.rsplit(maxsplit=2)[1] == '200'))
print(f'Общий трафик: {all_byte}, трафик по логу "200": {byte200}. Лог "200" составляет: '
      f'{byte200/all_byte * 100}% от общего трафика')

# task 2
byte404 = sum((int(i.rsplit(maxsplit=1)[1].replace('-', '0')) for i in wwwlog if i.rsplit(maxsplit=2)[1] == '404'))
print(f'Общий трафик: {all_byte}, трафик по логу "404": {byte404}. Лог "404" составляет: '
      f'{byte404/all_byte * 100}% от общего трафика')

# task 3
lnrow = sum((1 for i in wwwlog))
print(f'Количество запросов в файле: {lnrow}')

# task 4
byte200_dl = sum((1 for i in wwwlog if i.rsplit(maxsplit=2)[1] == '200'))
print(f'Количество запросов по логу "200": {byte200_dl}')

# task 5
byte404_dl = sum((1 for i in wwwlog if i.rsplit(maxsplit=2)[1] == '404'))
print(f'Количество запросов по логу "404": {byte404_dl}')

# task 6
print(f'В среднем по логу "200" тратиться: {byte200/byte200_dl} байт, а по "404" тратиться: {byte404/byte404_dl} байт')

# task 7
unique_ip = []
[unique_ip.append(i.split(maxsplit=1)[0]) for i in wwwlog if i.split(maxsplit=1)[0] not in unique_ip]
print(unique_ip)
k = lambda x: int(x[:2])
print(sorted(unique_ip, key=k, reverse=True))

# task 8
print(f'Количество уникальных IP: {len(unique_ip)}')

# task 9
dt_ip = []
[dt_ip.append(i.split(maxsplit=1)[0]) for i in wwwlog if i.split(maxsplit=1)[0] not in dt_ip and
 dt.datetime.strptime(i.split()[3].split(':', maxsplit=1)[1], '%H:%M:%S').time() < dt.time(12, 00)]
print(dt_ip)

# task 10
second_half = []
[second_half.append(i.split(maxsplit=1)[0]) for i in wwwlog if i.split(maxsplit=1)[0] not in second_half and
 dt.datetime.strptime(i.split()[3].split(':', maxsplit=1)[1], '%H:%M:%S').time() > dt.time(12, 00)]


if len(dt_ip) > len(second_half):
    print(f'Количество IP в первой половине дня: {len(dt_ip)}, во второй: {len(second_half)}. Трафик больше до полудня')
else:
    print(f'Количество IP в первой половине дня: {len(dt_ip)}, во второй: {len(second_half)}. Трафик больше после полудня')