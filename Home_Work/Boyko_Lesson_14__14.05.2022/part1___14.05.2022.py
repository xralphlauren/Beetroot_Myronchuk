# task 1.1
lst_1 = [str(i) for i in range(int(input('Введите число: '))+1)]
print(lst_1)

# task 1.2
lists = ['кит', 'кот', 'крот', 'конь', 'мышь', 'жираф', 'слон']
lst_2 = [str(i) + lists[i] for i in range(len(lists))]
print(lst_2)

# task 1.3
lst_3 = [str(i) + lists[i] for i in range(len(lists)) if len(lists[i]) <= 3]
print(lst_3)

# task 1.4
lists = ['111', 'cat', 'got', 'ddd', '222', '555555', 'horse', 'elephant']
lst_4 = [i for i in lists if i.isdigit()]
print(lst_4)

# task 1.5
lst_5 = [lists.index(i) for i in lists if i.isdigit()]
print(lst_5)

# task 1.6
lst_6 = [(lists.index(i), i) for i in lists if i.isdigit()]
print(lst_6)

# task 1.7
phones = ['044 225 73 39', '099 116 30 87', '094 129 81 69', '094 127 04 85', '044 222 74 33', '044 353 55 31',
          '097 921 27 09', '094 550 50 02', '044 362 96 00', '097 853 55 81', '097 120 95 90', '099 752 22 97',
          '050 761 49 45', '094 497 75 09', '094 498 89 53', '094 496 13 91', '094 497 35 13', '094 497 75 69',
          '050 063 52 97', '050 530 97 71', '044 227 16 63', '056 785 55 19', '068 450 69 13', '097 001 42 67',
          '096 097 58 16', '094 497 34 37', '094 097 12 17', '094 497 75 69', '097 497 75 97', '094 497 34 85',
          '094 496 52 54']
lst_7 = [i for i in phones if i[0:3] == '097']
print(lst_7)

# task 1.8
lst_8 = [i for i in phones if i[0:3] == '097' or i[0:3] == '050']
print(lst_8)

# task 1.9
lst_9 = ['+38' + i.replace(' ', '') for i in phones if i[0:3] == '097' or i[0:3] == '050']
print(lst_9)

