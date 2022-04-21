file = open('Daily Observations.txt', 'r')
read = file.readlines()
Humidity = 0

for i in read:
    if 'Humidit' in i.split()[4][:-1]:          # Пропускаю первую строку ( заголовок )
        continue
    Humidity += int(i.split()[4][:-1])

print(f'Среедняя влажность составляет: {Humidity/len(read)}')