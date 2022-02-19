import random

lst_1 = [random.randint(1, 100) for i in range(1, 10)]
lst_2 = [random.randint(1, 100) for y in range(1, 10)]
print(lst_1) # проверка листа 1
print(lst_2) # проверка листа 2

lst_3 = []
for i in lst_1:
    for j in lst_2:
        if i == j:
            lst_3.append((i, j))

print(lst_3)