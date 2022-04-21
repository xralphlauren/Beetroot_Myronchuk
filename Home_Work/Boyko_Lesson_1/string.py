fio = 'Мирончук Дмитрий Сергеевич'
print(len(fio))

name, fam, otch = fio.split()[0], fio.split()[1], fio.split()[2]
print(name, fam, otch)

print(fio.count('о'))
print(fio.count('е'))

fio1 = f'Мирончук\nДмитрий\tСергеевич'
print(fio1)