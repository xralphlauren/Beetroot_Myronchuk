import random

a = list(input())
for i in range(5):
    random.shuffle(a)
    for j in a:
        print(j, end="")
    print()
