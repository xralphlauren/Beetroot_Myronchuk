# Old variant
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

# new variant

v2_lst_1 = []
v2_lst_2 = []
i = 1
while i < 100:
    v2_lst_1.append(i)
    i += 1

i = 0
while i < len(v2_lst_1):
    if v2_lst_1[i] % 7 == 0 and v2_lst_1[i] % 5 != 0:
        v2_lst_2.append(v2_lst_1[i])
    i += 1

print(v2_lst_2)