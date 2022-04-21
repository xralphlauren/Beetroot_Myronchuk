f = open('weather.log', 'r', encoding='utf-8')
t = f.readlines()
f.close()
s = 0
count = 0

for i in t:
    if '-09-' in i.split()[0]:
        temp_txt = i.split()[2]
        temp_int = int(temp_txt.replace('°C,', ''))
        s = s + temp_int
        count += 1

print(f'Средняя температура за сентябрь составила: {s / len(t)} °C. Количество день вошедних в подсчёт: {count}')