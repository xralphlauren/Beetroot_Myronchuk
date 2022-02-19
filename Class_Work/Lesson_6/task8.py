import random
lst = [i for i in range(random.randint(1,100))]
lst = [x for x in lst if not int(x) % 2]
print(lst)






lst_2 = []
lst_3 = []
for i in range(1, random.randint(1,100)):
    lst_2.append(i)
for i in lst_2:
    if i % 2 == 0:
        lst_3.append(i)

print(lst_3)