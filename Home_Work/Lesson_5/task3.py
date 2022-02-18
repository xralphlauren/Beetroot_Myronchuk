import random

lst_1 = []
lst_2 = []
i = 0
while i < 100:
    lst_1.append(random.randint(1, 100))
    i += 1

i = 0
while i < len(lst_1):
    if lst_1[i] % 7 == 0 and lst_1[i] % 5 != 0:
        lst_2.append(lst_1[i])
    i += 1

print(lst_2)
