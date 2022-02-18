import random

i = 0
lst_1 = []
lst_2 = []

while i < 10:
    lst_1.append(random.randint(1, 10))
    lst_2.append(random.randint(1, 10))
    i += 1

lst_3 = list(set(lst_1) & set(lst_2))
print(lst_3)
