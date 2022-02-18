import random

lst = []
i = 0

while i < 10:
    a = random.randint(1, 10000)
    lst.append(a)
    i += 1

print(max(lst))
