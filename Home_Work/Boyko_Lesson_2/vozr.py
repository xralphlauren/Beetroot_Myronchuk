file = open('C:/Python/Beetroot/fio.txt', 'r')
file_read = file.readlines()
name = file_read[0].split()[1]
year = file_read[1].split('.')[2]
file.close()

print(f'Добрый день {name}! Ваш возраст {2022 - int(year)} лет!')
