file = open('file_for_5task', 'r')
read = file.readlines()
min_salary = float(read[1].split(';')[2][1:].replace(',', ''))
name_min_salary = read[1].split(';')[0]
max_salary = float(read[1].split(';')[2][1:].replace(',', ''))
name_max_salary = read[1].split(';')[0]
total_salary = 0
count = 0
staff_count = 0
staff_total_salary = 0
salary_0 = ''
for i in read[1:]:
    x = float(i.split(';')[2][1:].replace(',', ''))
    count += 1

    # высчитываю минимальную ЗП
    if 0 < x < min_salary:                      # убираю варианты с ЗП 0
        min_salary = x
        name_min_salary = i.split(';')[0]
    # высчитываю максимальную ЗП
    if x > max_salary:
        max_salary = x
        name_max_salary = i.split(';')[0]
    # высчитываю среднюю ЗП
    total_salary += x
    # высчитываю количество STAFF ASSISTANT и их среднюю ЗП
    if 'STAFF ASSISTANT' in i.split(';')[-1]:
        staff_count += 1
        staff_total_salary += x
    # высчитываю людей которым не платят зп
    if x == 0:
        salary_0 += i.split(';')[0] + '; '


print(read)
print(f'Меньше всего в Белом Доме зарабатывает: {name_min_salary}, сума составила: {min_salary}')   # task 1
print(f'Больше всего в Белом Доме зарабатывает: {name_max_salary}, сума составила: {max_salary}')   # task 2
print(f'Средняя заработная плата в Белом доме составила: {total_salary/count}')                     # task 3
print(f'Количество STAFF ASSISTANT в белом доме составляет: {staff_count}')                         # task 7
print(f'Средняя заработная плата STAFF ASSISTANT составляет: {staff_total_salary/staff_count}')     # task 8
print(f'Люди которым не платят: {salary_0}')                                                        # task 9