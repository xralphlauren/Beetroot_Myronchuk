import random

lst = []
tpl = ()
i = random.randint(1, 100)
while i != 0:
    lst.append(random.randint(1, 1000))
    tpl += (random.randint(1, 1000),)
    i -= 1

print(sum(lst)/len(lst))
print(sum(tpl)/len(tpl))

lst_copy = lst.copy()
print(lst_copy)